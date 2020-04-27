import abc
import pandas as pd

from .feature import FeatureDataFrame


class FeatureFactory(abc.ABCMeta):

    @abc.abstractstaticmethod
    def make(dataset_df: pd.DataFrame) -> FeatureDataFrame:
        raise NotImplementedError("未実装.")
