import abc


class BaseLoader:
    def __init__(
        self,
    ):
        pass

    @abc.abstractmethod
    def load(self):
        """
        load data to destination storage
        """
        pass
