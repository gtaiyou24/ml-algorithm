import numpy as np
import pandas as pd
from lifelines import CoxPHFitter
from sksurv.util import check_arrays_survival

from .survival_analysis_estimator import AbstractSAThresholdPredicter


class CoxSAEstimator(CoxPHFitter, AbstractSAThresholdPredicter):
    """Cox比例ハザードモデル.

    Parameters
    ----------
    alpha : float, optional, default: 0.95
        信頼係数.
    verbose: bool, optional, default: False
        デバック情報を出力するか否かを指定.
    strat_list : list, optional, default: None
        層別変数名を指定.この指定した層別変数の値ごとに閾値を計算する.

    Attributes
    ----------
    w_ : ndarray, shape = (n_features,)
        モデルの回帰係数.
    feature_name_list : list,
        説明変数名を格納したリスト.

    References
    ----------
    .. [1] デビッド・ホスマー, スタンリー・レメンショウ, スーザン・メイ[2014]『生存時間解析入門[原書第2版]』(P.71-95)
    """

    def __init__(self, alpha=0.95, verbose=False, strat_list=None):
        """init."""
        self.verbose = verbose
        self.strat_list = strat_list
        super().__init__(strata=strat_list)

    def fit(self, X, y):
        """パラメータの推定を行う.

        Parameters
        ----------
        X : pandas.DataFrame, shape = (n_samples, n_features)
            Data matrix
        y : structured array, shape = (n_samples,)
            [(打切り変数, 観測時間), ...]

        Returns
        -------
        self
        """
        # lifelines.CoxPHFitter の fit() に渡すためのデータフレームを整形.
        feature_name_list = X.columns.values.tolist()
        name_event, name_time = y.dtype.names

        x, event, time = check_arrays_survival(X, y)

        y_df = pd.DataFrame([time, event]).T
        y_df.columns = [name_time, name_event]

        x_df = pd.DataFrame(x, columns=feature_name_list)

        df = pd.merge(x_df, y_df, left_index=True, right_index=True)

        super().fit(df, duration_col=name_time, event_col=name_event, strata=self.strat_list)

        # self.w_ は attribute で残しときたい.
        self.w_ = self.hazards_.values[0]
        self.feature_name_list = feature_name_list

        return self

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
        if isinstance(X, np.ndarray):
            X = pd.DataFrame(X, columns=self.feature_name_list)

        survival_df = super().predict_survival_function(X, times)
        return survival_df.values

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
        dead_function_arr = self._predict_dead_function(X, times)
        survival_arr = 1 - dead_function_arr

        hazard_arr = (dead_function_arr[1:] - dead_function_arr[:-1]) / survival_arr[:-1]

        return hazard_arr
