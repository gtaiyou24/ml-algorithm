import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from ...domain.model.dataset import DatasetFactory
from ...domain.model.estimator import Classifier,
from ...domain.model.feature import FeatureFactory
from ...domain.model.teacher import TeacherFactory
from ...domain.repository import ClassifierRepository
from ...domain.service import FilterService


class TrainEstimatorUsecase:

    def __init__(self, feature_factory: FeatureFactory, teacher_factory: TeacherFactory,
        filter_service: FilterService, classifier_repository: ClassifierRepository):
        self.feature_factory = feature_factory
        self.teacher_factory = teacher_factory
        self.filter_service = filter_service
        self.dataset_factory = DatasetFactory()
        self.classifier_repository = classifier_repository

    def train(self):
        # 1. アイテム,ユーザデータの取得
        item_df = pd.DataFrame([])
        user_df = pd.DataFrame([])
        # ... その他データ
        recommend_ids = pd.MultiIndex([], names=['user_id', 'item_id'])

        # 2. 特徴量/教師データの生成
        feature = self.feature_factory.make(recommend_ids, item_df, user_df)
        teacher = self.teacher_factory.make(recommend_ids, item_df, user_df)

        # 3. アイテムフィルタリング
        feature = feature.loc[self.filter_service.recommendable_ids(recommend_ids, item_df, user_df)]
        teacher = teacher.loc[self.filter_service.recommendable_ids(recommend_ids, item_df, user_df)]

        # 4. データセットの作成
        dataset_df = self.dataset_factory.make(teacher, feature)

        # 5. モデル学習
        classifier = Classifier('モデル名_v1_20200507', RandomForestClassifier(class_weight='balanced'))
        classifier.estimator.train(dataset_df.features, dataset_df.teachers)

        # 6. 評価
        classifier.confusion(dataset_df.features, dataset_df.teachers)
        classifier.metrics(dataset_df.features, dataset_df.teachers)

        # 6. モデル保存
        self.classifier_repository.save(classifier)
