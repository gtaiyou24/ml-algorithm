"""ε-貪欲法モデルを定義したクラス."""
from .abstract_bandit_model import AbstractBanditAlgo


class EpsilonGreedy(AbstractBanditAlgo):
    """
    ε-貪欲法モデル.

    Parameters
    ----------
    epsilon : float, [0, 1].
            ε(イプシロン)パラメータ.
    """

    def __init__(self, epsilon=0.1):
        """init."""
        self.epsilon = epsilon
