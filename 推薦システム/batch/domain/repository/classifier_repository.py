import abc

from ..model.classifier import Classifier


class ClassifierRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, classifier: Classifier) -> None:
        pass

    @abc.abstractmethod
    def get(self, id: str) -> Classifier:
        pass
