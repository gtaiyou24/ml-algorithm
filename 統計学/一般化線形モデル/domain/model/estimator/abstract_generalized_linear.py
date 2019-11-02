"""一般化線形モデルが継承する抽象クラス."""

import abc

from sklearn.base import BaseEstimator


class AbstractGeneralizedLinearModel(abc.ABC, BaseEstimator):
    """
    Abstract Generalized Linear Model.

    すべての一般化線形モデルが以下の関数をもつことを強制するための抽象クラス.
     - fit() : 最尤推定処理を行うメソッド.
     - score() : スコア統計量を算出するメソッド.
    """

    pass
