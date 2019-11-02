import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

from ..rating import RatingDataFrame


class UserBaseCF(BaseEstimator):

    def fit(self, rating_df: RatingDataFrame):
        self.rating_df = rating_df.copy()
        self.user_similarity_df = self._similarity_of_users(rating_df)
        self.mean_rating_of_user_ser = self._mean_rating_of_user(rating_df)
        # self.mean_rating_to_item_ser = self._mean_rating_to_item(rating_df)

    def _similarity_of_users(self, rating_df: RatingDataFrame) -> pd.DataFrame:
        """
        ユーザ同士の類似度(ピアソン相関係数)を計算し、データフレームで返す.
        ただし、対角成分(同一ユーザでの類似度1.0)は0.0にする.
        """
        similarity_of_user_df = rating_df.T.corr(method='pearson').copy()
        np.fill_diagonal(similarity_of_user_df.values, 0.0)
        return similarity_of_user_df.copy()

    def _mean_rating_of_user(self, rating_df: RatingDataFrame) -> pd.Series:
        """ユーザごとの平均評価値を計算."""
        return rating_df.mean(axis=1)

    # def _mean_rating_to_item(self, rating_df: RatingDataFrame) -> pd.Series:
    #     """アイテムごとの平均評価値を計算."""
    #     return rating_df.mean()

    def _similarity_user_ids(self, item_id, user_id) -> pd.Index:
        """
        アイテム(item_id)を評価したユーザ(user_id)に類似するユーザIDを取得する.
        """
        is_already_rated_item = self.rating_df[item_id].notnull()
        user_id_already_rated = self.rating_df.loc[is_already_rated_item].index
        similarity = self.user_similarity_df.loc[user_id, user_id_already_rated]
        return similarity.sort_values(ascending=False).index.tolist()

    def predict(self, user_id, item_id) -> float:
        other_user_ids = self._similarity_user_ids(item_id, user_id)
        weight_ser = self.user_similarity_df.loc[user_id, other_user_ids]

        base_rating_of_user = self.mean_rating_of_user_ser.loc[user_id]
        y_lj = self.rating_df.loc[other_user_ids, item_id]
        y_l = self.mean_rating_of_user_ser.loc[other_user_ids]

        return base_rating_of_user + (
            (weight_ser * (y_lj - y_l)).sum() / weight_ser.abs().sum()
        )
