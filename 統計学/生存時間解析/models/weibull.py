import numpy as np
from scipy.linalg import solve
from sklearn.utils.validation import check_is_fitted
from sksurv.util import check_arrays_survival

from .survival_analysis_estimator import AbstractSAThresholdPredicter


class WeibullRMLogLikelihood(object):
    """ワイブル回帰モデルの対数尤度関数を定義. ニュートン・ラフソン法でパラメータを推定を行う."""

    def __init__(self, X, event, time, alpha):
        """init."""
        self.x = X
        self.event = event
        self.time = time
        self.alpha = alpha

    def update(self, parameters, offset=0):
        """勾配ベクトルとヘッセ行列を計算し、ニュートン・ラフソン法でパラメータを更新する."""
        x = self.x
        n_samples, n_features = x.shape

        w = parameters[:-1]
        sigma = parameters[-1]

        grad_list = []
        for j in range(w.shape[0]):
            grad_list.append(self._dw_logL(w, sigma, j))
        grad_list.append(self._dsigma_logL(w, sigma))
        grad_logL = np.array(grad_list)

        hessian = np.zeros((n_features + 1, n_features + 1), dtype=float)

        for j in range(w.shape[0]):
            for k in range(w.shape[0]):
                hessian[j][k] = self._dwdw_logL(w, sigma, j, k)
            hessian[j][-1] = self._dwdsigma_logL(w, sigma, j)

        for k in range(w.shape[0]):
            hessian[-1][k] = self._dwdsigma_logL(w, sigma, k)
        hessian[-1][-1] = self._dsigmadsigma_logL(w, sigma)

        self.gradient = grad_logL
        self.hessian = hessian

        return self

    def _dw_logL(self, w, sigma, j):
        x = self.x
        time = self.time
        dw_logL = 0
        z = (np.log(time) - np.dot(x, w)) / sigma
        event = np.where(self.event, 1, 0)
        dw_logL_ser = -(x[:, j] / sigma) * (event - np.exp(z))
        dw_logL = dw_logL_ser.sum()
        return dw_logL

    def _dsigma_logL(self, w, sigma):
        x = self.x
        m = self.event[self.event == 1].shape[0]

        time = self.time
        event = np.where(self.event, 1, 0)
        z = (np.log(time) - np.dot(x, w)) / sigma
        dsigma_logL_ser = (z / sigma) * (event - np.exp(z))
        return -(m / sigma) - dsigma_logL_ser.sum()

    def _dwdw_logL(self, w, sigma, j, k):
        x = self.x
        v = 0

        time = self.time
        z = (np.log(time) - np.dot(x, w)) / sigma
        v_ser = x[:, j] * x[:, k] * np.exp(z)
        v = v_ser.sum()
        return -(1 / sigma ** 2) * v

    def _dwdsigma_logL(self, w, sigma, j):
        x = self.x
        v = 0

        time = self.time
        z = (np.log(time) - np.dot(x, w)) / sigma
        v_ser = x[:, j] * z * np.exp(z)
        v = v_ser.sum()
        return -v / (sigma ** 2)

    def _dsigmadsigma_logL(self, w, sigma):
        x = self.x
        m = self.event[self.event == 1].shape[0]

        v = 0
        time = self.time
        z = (np.log(time) - np.dot(x, w)) / sigma
        v_ser = (z ** 2) * np.exp(z)
        v = v_ser.sum()
        return -m / (sigma ** 2) - v / (sigma ** 2)


class WeibullSACareerEstimator(AbstractSAThresholdPredicter):
    """ワイブル回帰モデル. ニュートン・ラフソン法を用いて最適化する.

    Parameters
    ----------
    alpha : float, optional, default: 0
        ridge回帰ペナルティのための正則化パラメータ。
    n_iter : int, optional, default: 100
        パラメータ更新の最大回数を指定.
    tol : float, optional, default: 1e-9
        ニュートン法の収束値を指定.
    verbose: bool, optional, default: False
        デバック情報を出力するか否かを指定.
    strat_list : list, optional, default: None
        層別変数名を指定。この指定した層別変数の値ごとに閾値を計算する.

    Attributes
    ----------
    w_ : ndarray, shape = (n_features,)
        ワイブル回帰モデルの回帰パラメータ.
    lambda_: float,
        ワイブル回帰モデルの形状パラメータ.
    hessian: ヘッセ行列.
    gradient: 勾配ベクトル.

    References
    ----------
    .. [1] デビッド・ホスマー, スタンリー・レメンショウ, スーザン・メイ[2014]『生存時間解析入門[原書第2版]』(P.71-289)
    """

    def __init__(self, alpha=0, n_iter=100, tol=1e-9, verbose=False, strat_list=None):
        """init."""
        if alpha < 0:
            raise ValueError('alpha must be positive, but was %r' % alpha)
        self.alpha = alpha
        self.n_iter = n_iter
        self.tol = tol
        self.verbose = verbose
        self.strat_list = strat_list

    def fit(self, X, y):
        """パラメータの推定を行う.

        Parameters
        ----------
        X : array-like, shape = (n_samples, n_features)
            Data matrix
        y : structured array, shape = (n_samples,)
            [(打切り変数, 観測時間), ...]

        Returns
        -------
        self
        """
        X, event, time = check_arrays_survival(X, y)

        if self.alpha < 0:
            raise ValueError('alpha must be positive, but was %r' % self.alpha)

        log_likelihood = WeibullRMLogLikelihood(X, event, time, self.alpha)

        verbose = self.verbose
        n_params = X.shape[1] + 1
        parameters = np.zeros(n_params)
        parameters[-1] = 0.5  # sigmaは分母として用いるので0
        i = 0
        while True:
            if i >= self.n_iter:
                if verbose:
                    print('iter {:>6d}: reached maximum number of iterations. Stopping.'.format(i + 1))
                print('Optimization did not converge: Maximum number of iterations has been exceeded.')
                break

            log_likelihood.update(parameters)
            delta = solve(log_likelihood.hessian, log_likelihood.gradient,
                          overwrite_a=False, overwrite_b=False, check_finite=False)

            if not np.all(np.isfinite(delta)):
                raise ValueError('search direction contains NaN or infinite values')

            parameters_new = parameters - delta

            if verbose:
                print('iter {: > 6d}: update={}'.format(i + 1, delta))

            parameters = parameters_new

            res = np.abs(delta)
            if np.all(res < self.tol):
                break
            else:
                i += 1

        self.w_ = parameters[:-1]
        self.sigma_ = parameters[-1]
        # self.hessian, self.gradient は attribute で残しときたい.
        self.hessian = log_likelihood.hessian
        self.gradient = log_likelihood.gradient
        return self

    def _dot_X_w(self, X):
        """リスクスコアを予測.

        Parameters
        ----------
        X : array-like, shape = (n_samples, n_features)
            Data matrix.

        Returns
        -------
        xw_ : array, shape = (n_samples,)
            リスクスコア.
        """
        check_is_fitted(self, 'w_')

        X = np.atleast_2d(X)

        return np.dot(X, self.w_)

    def _predict_survival_function(self, X, times):
        """
        特徴量xと時間tから生存確率を算出.

        Parameters
        ----------
        X: array-like, shape = (n_samples, n_features)
            Data matrix.
        times: array-like, shape = (n_times, )
            Data matrix.

        Returns
        -------
        survival : ndarray, shape = (n_times, n_samples)
            予測された生存関数.
        """
        lambda_ = 1 / self.sigma_
        xw_ = self._dot_X_w(X)
        n_samples = xw_.shape[0]
        n_times = times.shape[0]

        times = times.reshape((n_times, 1))
        xw_ = xw_.reshape((1, n_samples))

        return np.exp(-(times**lambda_) * np.exp(-lambda_ * xw_))

    def _predict_hazard_function(self, X, times):
        """
        特徴量xと時間tからハザード値を算出.

        Parameters
        ----------
        X: array-like, shape = (n_samples, n_features)
            Data matrix.
        times: array-like, shape = (n_times, )
            Data matrix.

        Returns
        -------
        survival : ndarray, shape = (n_times, n_samples)
            予測されたハザード関数.
        """
        lambda_ = 1 / self.sigma_
        xw_ = self._dot_X_w(X)
        n_samples = xw_.shape[0]
        n_times = times.shape[0]

        times = times.reshape((n_times, 1))
        xw_ = xw_.reshape((1, n_samples))

        return (lambda_ * times ** (lambda_ - 1)) * np.exp(- lambda_ * xw_)
