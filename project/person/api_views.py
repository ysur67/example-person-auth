from rest_framework import viewsets, generics
from person.serializers import UserCreateSerializer, RequestResultListSeriailzer
from person.models import RequestResult
from django.http import HttpResponse
import json
import datetime
from person.utils import (Mapper, ResponseToResultMapper,
                          BaseConverter, TxtConverter, XlsxConverter)


class PersonCreateView(viewsets.generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        mapper: Mapper = ResponseToResultMapper(response)
        mapper.convert()
        return response


class BaseDownloadFileView(generics.ListAPIView):
    model = None
    serializer_class = RequestResultListSeriailzer
    converter_class: BaseConverter = None

    FILE_NAME_TEMPLATE = "||"
    CONTENT_TYPE = ""

    def get(self, request, *args, **kwargs):
        filename = self.FILE_NAME_TEMPLATE.replace("||", str(datetime.date.today()))
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        converter = self.converter_class(serializer.data)
        output = converter.convert()
        response = HttpResponse(output, content_type=self.CONTENT_TYPE)
        response['Content-Disposition'] = ('attachment; filename={0}'.format(filename))
        return response

    def get_queryset(self):
        return self.model.objects.all()


class TxtDownloadFileView(BaseDownloadFileView):
    model = RequestResult
    converter_class = TxtConverter
    FILE_NAME_TEMPLATE = "requests-||.txt"
    CONTENT_TYPE = "text/plain; charset=UTF-8"
    

class XlsxDownloadFileView(BaseDownloadFileView):
    model = RequestResult
    converter_class = XlsxConverter
    FILE_NAME_TEMPLATE = "requests-||.xlsx"
    CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
