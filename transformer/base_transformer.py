import abc


class BaseTransformer:
    def __init__(
        self,
    ):
        pass

    @abc.abstractmethod
    def transform(self):
        pass
