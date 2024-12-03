from core.utils import SerializerUtils
from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()

class AccountBaseModelSerializer(SerializerUtils.BaseModelSerializer):
    class Meta(SerializerUtils.BaseModelSerializer.Meta):
        model = UserModel