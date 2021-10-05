from .base_converter import BaseConverter
import json


class TxtConverter(BaseConverter):
    def convert(self):
        data = json.dumps(self._initial, indent=4)
        self._result = data
        return self._result
