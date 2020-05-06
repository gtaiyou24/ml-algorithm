import abc
import pandas as pd


class FeatureFactory(abc.ABC):

    @abc.abstractmethod
    def make(self) -> pd.DataFrame:
        pass
