from rest_framework import response, viewsets, status
from person.serializers import UserCreateSerializer


class PersonCreateView(viewsets.generics.CreateAPIView):
    serializer_class = UserCreateSerializer
