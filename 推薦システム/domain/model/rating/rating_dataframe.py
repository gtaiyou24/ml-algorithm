import numpy as np

import pandas as pd


class RatingDataFrame(pd.DataFrame):
    def __init__(self, rating_matrix: np.array, user_id_list: list, item_id_list: list):
        super().__init__(rating_matrix, index=user_id_list, columns=item_id_list)
