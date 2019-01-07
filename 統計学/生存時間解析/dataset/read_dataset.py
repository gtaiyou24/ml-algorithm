u"""データセットの読み込み関数を定義."""

import os

from glob import glob

import pandas as pd


# データセットディレクトリのパス(本pythonファイルからの相対パス)を定義
SURVIVAL_DATASET_DIR_ABSPATH = '/{0}'


def _search_file_path(file_name='*'):
    u"""引数の値からファイルを検索し、合致したファイルの絶対パスを返す.

    Parameters
    ----------
    file_name : str, optional, default: '*'
                            検索するファイル名を文字列(正規表現)で指定.

    Return
    ------
    file_paths : list
    """
    dirname = os.path.dirname(os.path.abspath(__file__))
    search_file = dirname + SURVIVAL_DATASET_DIR_ABSPATH.format(file_name)
    return glob(search_file)


def read_whas100_df(names=['登録日(観察開始日)', '追跡日(観察終了日)', '入院期間', '追跡日数(観察日数)', '生存状態', '登録時年齢', '性別', 'BMI']):
    u"""
    WHAS100.datを読み込み、データフレームとして返す.

    Parameters
    ----------
    names: list, optional
           `pandas.read_csv`の引数`names`に指定するリスト.

    Return
    ------
    whas100_df : pandas.DataFrame
    """
    whas100_file_path = _search_file_path('whas100.dat')[0]

    whas100_df = pd.read_csv(
        whas100_file_path,
        sep='\s+',
        header=None,
        index_col=0,
        names=names
    )
    return whas100_df
