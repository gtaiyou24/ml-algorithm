import pandas as pd


class RegressionTeacherSeries(pd.Series):
    """回帰教師シリーズクラス."""

    def __init__(self, data, index):
        """回帰教師列を生成."""
        super().__init__(data, index)
        self.name = 'RegressionTeacher'
        self.index.name = 'index'
