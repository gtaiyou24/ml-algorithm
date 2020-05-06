import abc


class FilterService(abc.ABC):

    @abc.abstractmethod
    def recommendable_ids(self):
        pass

    @abc.abstractmethod
    def recommendable_item_ids(self):
        pass

    @abc.abstractmethod
    def recommendable_user_ids(self):
        pass
