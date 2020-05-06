import os
import pickle

from ....domain.model.classifier import Classifier
from ....domain.repository import ClassifierRepository


class LocalClassifierRepository(ClassifierRepository):

    def __init__(self, dump_dir: str):
        self.dump_dir = dump_dir

    def save(self, classifier: Classifier) -> None:
        pickle.dump(
            classifier,
            open(os.path.join(self.dump_dir, '{}.sav'.format(classifier.id)), 'wb')
        )

    def get(self, id: str) -> Classifier:
        return pickle.load(open(os.path.join(self.dump_dir, '{}.sav'.format(id)), 'rb'))
