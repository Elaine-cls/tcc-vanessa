from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        
class BaseModelExcludeSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('medical_history',)