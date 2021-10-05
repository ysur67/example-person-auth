from rest_framework import serializers
from person.models import User
from person.models.result import RequestResult


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("name", "birth_date",
                  "phone", "email",
                  "username", "password", )

    def get_password(self, instance):
        password = User.objects.make_random_password()
        return password

    def validate(self, attrs):
        if not attrs.get("phone", None) and not attrs.get("email", None):
            raise serializers.ValidationError("The value of phone and/or email is required")
        return super().validate(attrs)

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        instance.set_password(self.data["password"])
        instance.save()
        return instance


class RequestResultListSeriailzer(serializers.ModelSerializer):
    class Meta:
        model = RequestResult
        fields = "__all__"
