
import abc

import numpy as np

from sklearn.base import BaseEstimator


class AbstractSurvivalEstimator(abc.ABC, BaseEstimator):
    """
    Abstract Survival Analysis Career Estimator.

    すべての生存時間解析モデルが以下の関数をもつことを強制するための抽象クラス.
     - fit() : 学習処理を行うメソッド.
     - predict_survival_function() : 生存関数を算出するメソッド.
    """

    @abc.abstractmethod
    def fit(self, X, y):
        """モデルの学習処理."""
        pass

    @abc.abstractmethod
    def _predict_survival_function(self, X, times):
        pass

    @abc.abstractmethod
    def _predict_hazard_function(self, X, times):
        pass

    def _predict_cumulative_hazard_function(self, X, times):
        """
        特徴量xと時間tから累積ハザード値を算出.

            H(x,t) = - log[S(x,t)]

        Parameters
        ----------
        X: array-like, shape = (n_samples, n_features)
            Data matrix
        times: array-like, shape = (n_times,)

        Returns
        -------
        cumulative_hazard : ndarray, shape = (n_times, n_samples)
            予測された累積ハザード.
        """
        return - np.log(self._predict_survival_function(X, times))

    def _predict_dead_function(self, X, times):
        """
        特徴量Xと時間tから死亡確率を算出.

            F(x,t) = 1 - S(x,t)

        Parameters
        ----------
        X: array-like, shape = (n_samples, n_features)
            Data matrix
        times: array-like, shape = (n_times,)

        Returns
        -------
        dead : ndarray, shape = (n_times, n_samples)
            予測された死亡関数.
        """
        return 1 - self._predict_survival_function(X, times)
