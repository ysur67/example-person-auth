from abc import ABC, abstractmethod


class BaseConverter(ABC):
    _result = None

    def __init__(self, initial_data) -> None:
        self._initial = initial_data

    @property
    def data(self):
        """Конвертированное значение."""
        if self._result is None:
            raise ValueError("It is impossible to get value before conversion")
        return self._result

    @abstractmethod
    def convert(self):
        """Конвертировать переданное значение."""
        pass
