from .base_converter import BaseConverter
import pandas
from io import BytesIO


class XslConverter(BaseConverter):
    def convert(self):
        sio = BytesIO()
        PandasDataFrame = pandas.DataFrame(self._initial)
        PandasWriter = pandas.ExcelWriter(sio, engine='xlsxwriter')
        PandasDataFrame.to_excel(PandasWriter, sheet_name="0")
        PandasWriter.save()
        sio.seek(0)
        self._result = sio.getvalue()
        return self._result
