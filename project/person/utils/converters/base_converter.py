from abc import ABC, abstractmethod


class BaseConverter(ABC):
    _result = None
    def __init__(self, initial_data: dict) -> None:
        self._initial = initial_data

    @property
    def data(self):
        return self._result
    
    @abstractmethod
    def convert(self):
        pass
