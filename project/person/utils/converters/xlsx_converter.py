from .base_converter import BaseConverter
import pandas
from io import BytesIO


class XlsxConverter(BaseConverter):
    def convert(self):
        output = BytesIO()
        PandasDataFrame = pandas.DataFrame(self._initial)
        PandasWriter = pandas.ExcelWriter(output, engine='xlsxwriter')
        PandasDataFrame.to_excel(PandasWriter, sheet_name="0")
        PandasWriter.save()
        output.seek(0)
        self._result = output.getvalue()
        return self._result
