import numpy as np
from scipy import optimize
from scipy.linalg import solve
from sklearn.utils.validation import check_is_fitted
from sksurv.util import check_arrays_survival

from .survival_analysis_estimator import AbstractSurvivalEstimator


def logistic_log_likelihood(weight_arr, *args):
	"""生存時間交差エントロピー."""
    X = args[0]
    event = args[1]
    time = args[2]
    id_ = args[3]

    event = np.where(event, 1, 0)

    z = np.dot(weight_arr, X)
    log_likelihood = event * np.log(-1 - np.exp(-z)) + (1 - event) * np.log(1 - 1 / (1 + np.exp(-z)))

    return -1 * log_likelihood


class LogisticSurvivalAnalysis(AbstractSurvivalEstimator):
    """ロジスティックハザードモデル."""

    def __init__(self, alpha=0):
        self.alpha = alpha

    def fit(self, X, y, id_):
        """モデルの学習処理.

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

        init_parameters = np.zeros(X.shape[1])

        parameter = optimize.minimize(logistic_log_likelihood, init_parameters, args=(X, event, time, id_), method='Nelder-Mead')
        print(parameter)
        return self

    def _predict_survival_function(self, X, times):
        """生存関数を返す.
        
        X : array-like, shape = (n_samples, n_features)
        times : array-like
        """
        pass

    def _predict_hazard_function(self, X, times):
        """ハザード関数を返す."""
        pass
