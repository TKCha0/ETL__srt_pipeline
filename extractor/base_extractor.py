import abc


class BaseExtractor:
    def __init__(
        self,
    ):
        pass

    @abc.abstractmethod
    def extract(self):
        pass
