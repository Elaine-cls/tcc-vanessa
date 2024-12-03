from .base_serializer import *
from ...models import Vet
from authentication.api.serializers import AccountCreateSerializer, AccountSerializer

class VetSaveSerializer(serializers.ModelSerializer):
    account = AccountCreateSerializer(read_only=True)
    class Meta:
        model = Vet
        exclude = ('clinic',)

class VetSerializer(BaseModelSerializer):
    account = AccountSerializer(read_only=True)
    class Meta(BaseModelSerializer.Meta):
        model = Vet
        
        