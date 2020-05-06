from ....domain.model.classifier import Classifier
from ....domain.repository import ClassifierRepository


class S3ClassifierRepository(ClassifierRepository):

    def __init__(self):
        pass

    def save(self, classifier: Classifier) -> None:
        raise NotImplementedError("S3用のClassifierRepositoryが未実装です.")

    def get(self, id: str) -> Classifier:
        raise NotImplementedError("S3用のClassifierRepositoryが未実装です.")
