from rest_framework import viewsets
from person.serializers import UserCreateSerializer
from person.utils import Mapper, ResponseToResultMapper


class PersonCreateView(viewsets.generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        mapper: Mapper = ResponseToResultMapper(response)
        mapper.convert()
        return response
