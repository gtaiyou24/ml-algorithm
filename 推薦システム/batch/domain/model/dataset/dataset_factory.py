import pandas as pd


class DatasetFactory:

    def make(self, teacher: pd.DataFrame, feature: pd.DataFrame) -> pd.DataFrame:
        dataset_df = pd.merge(
            pd.DataFrame(teacher.values, index=teacher.index, columns=[['teachers' for i in teacher.columns], teacher.columns]),
            pd.DataFrame(feature.values, index=feature.index, columns=[['features' for i in feature.columns], feature.columns]),
            left_index=True, right_index=True, how='left')
        return dataset_df.dropna()
