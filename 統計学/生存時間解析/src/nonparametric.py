u"""
ノンパラメトリック分析で用いる推定量,検定関数等を定義したモジュール.

生存関数の推定
------------
 - 生存関数の分散推定量
 - Kaplan-Meier関数の区間推定関数
 - 生存関数の信頼幅推定関数
 - 分位点推定関数
 - 分位点の区間推定関数

累積ハザード関数の推定
-------------------
 - Nelson-Aalen関数の区間推定関数

ハザード関数の推定
---------------
 - ハザード推定関数(Nelson-Aalen関数から導出)
 - カーネル平滑化関数

ノンパラメトリック検定
-------------------
 - ログランク検定関数
 - Wilcoxon検定関数
 - Tarone-Ware検定関数
 - Peto-Prentice検定関数
"""
import numpy as np

from sklearn.utils.validation import check_consistent_length

from sksurv.nonparametric import (
    _compute_counts,
    kaplan_meier_estimator
)
from sksurv.util import check_y_survival


__all__ = [
    "calc_kaplan_meier_variance",
]


def calc_kaplan_meier_variance(event, time):
    """Variance estimator of Kaplan-Meier survival function.

    Parameters
    ----------
    event : array-like, shape = (n_samples,)
        Contains binary event indicators.
    time : array-like, shape = (n_samples,)
        Contains event/censoring times.

    Return
    ------
    uniq_times : array, shape = (n_times,)
        Unique times.

    variance : array, shape = (n_times,)
        variance estimator of kaplan-meier survival function.

    References
    ----------
    .. [1]
    """
    event, time = check_y_survival(event, time)
    check_consistent_length(event, time)
    uniq_times, n_events, n_at_risk = _compute_counts(event, time)

    prob_survival = kaplan_meier_estimator(event, time)[1]
    variance = (prob_survival**2) * np.cumsum(n_events / (n_at_risk * (n_at_risk - n_events)))
    return uniq_times, variance


def kalbfleisch_prentice_interval_estimator():
    """Interval estimator defiend by Kalbfleisch and Prentice(2002).

    Parameters
    ----------
    """
    pass
