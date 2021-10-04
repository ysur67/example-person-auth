from rest_framework import serializers
from person.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "birth_date",
                  "phone", "email", "username", )

    def create(self, validated_data):
        return User.objects.create(**validated_data)
