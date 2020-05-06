import pandas as pd
import numpy as np

from datetime import datetime
from sklearn.base import BaseEstimator
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score


class Classifier:
    """
    Classifier.

    全ての二値分類推定器(モデル)が以下の関数をもつことを強制するためのクラス.

     - fit() : 学習処理を行うメソッド.
     - predict() : 予測値を算出するメソッド.
     - confusion() : 分割表を表示するメソッド.
     - metrics() : 評価指標を表示するメソッド.
    """
    def __init__(self, id: str, estimator: BaseEstimator):
        self.id = id
        self.estimator = estimator
        self.confusion_df = None
        self.metrics_ser = None

    def id(self):
        return self.id

    def confusion(self, X, y) -> pd.DataFrame:
        """分割表を表示."""
        if self.confusion_df is None:
            self.confusion_df = pd.DataFrame(
                confusion_matrix(y, self.estimator.predict(X)),
                index=['0(負)', '1(正)'], columns=['0(負)と予測', '1(正)と予測']
            )
        return self.confusion_df

    def metrics(self, X, y) -> pd.Series:
        """評価指標を表示."""
        if self.metrics_ser is None:
            confusion_df = self.confusion(X, y)
            y_pred       = self.estimator.predict(X)
            n            = y.shape[0]

            self.metrics_ser = pd.Series({
                '評価データサイズ': n,
                '正率': (confusion_df.loc['1(正)'].sum() / n).round(3),
                '負率': (confusion_df.loc['0(負)'].sum() / n).round(3),
                '偽陽性率(false positive rate)': (confusion_df.loc['0(負)', '1(正)と予測'] / confusion_df.loc['0(負)'].sum()).round(3),
                '真陽性率(true positive rate)': (confusion_df.loc['1(正)', '1(正)と予測'] / confusion_df.loc['1(正)'].sum()).round(3),
                '正確度(accuracy)': accuracy_score(y, y_pred).round(3),
                '適合率(precision)': precision_score(y, y_pred).round(3),
                '再現率(recall)': recall_score(y, y_pred).round(3),
                'F値(F-measure)': f1_score(y, y_pred).round(3)},
                name=self.id
            )

        return self.metrics_ser
