from rest_framework import serializers

class SerializerUtils:
    class BaseModelSerializer(serializers.ModelSerializer):
        class Meta:
            fields = '__all__'
    class BaseModelExcludeSerializer(serializers.ModelSerializer):
        class Meta:
            exclude = ['id']