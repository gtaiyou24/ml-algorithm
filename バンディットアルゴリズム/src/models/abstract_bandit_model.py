"""すべてのバンディットモデルが継承する抽象クラス."""
import abc

from sklearn.base import BaseEstimator


class AbstractBanditAlgo(abc.ABC, BaseEstimator):
    """
    Abstract Bandit Model.

    すべてのバンディットモデルが以下の関数をもつことを強制するための抽象クラス.
     - select_arm() : アームの選択を行うメソッド.
     - update() : パラメータの更新を行うメソッド.
    """

    def __init__(self, K):
        """
        init.

        Parameters
        ----------
        K : int
            アームの数.
        """
        self.K = K

    @abc.abstractmethod
    def select_arm(self):
        """腕の選択."""
        pass

    @abc.abstractmethod
    def update(self, x):
        """
        パラメータの更新.

        Parameters
        ----------
        x : float
            報酬.
        """
        pass
