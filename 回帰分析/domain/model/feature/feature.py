import pandas as pd


class FeatureDataFrame(pd.DataFrame):

    def __init__(self, index: pd.Index, column_names: list):
        if not isinstance(index, pd.Index):
            raise TypeError("引数indexがpd.Index型ではありません.")

        super(FeatureDataFrame, self).__init__(
            [],
            index=index,
            columns=[['features' for i in column_names], column_names]
        )
        self.index.name = 'index'

    @staticmethod
    def of(df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("引数ohlc_dfがpd.DataFrame型ではありません.")

        featureDataFrame = FeatureDataFrame(df.index, df.columns.tolist())
        featureDataFrame['features'] = df.round(3).copy()
        return featureDataFrame
