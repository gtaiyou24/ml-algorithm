import abc
import pandas as pd


class TeacherFactory(abc.ABC):

    @abc.abstractmethod
    def make(self) -> pd.DataFrame:
        pass
