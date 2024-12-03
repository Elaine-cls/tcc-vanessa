from .base_serializer import *
from authentication.api.serializers import AccountSerializer
from .address_serializer import AddressSerializer
from ...models import Owner

class OwnerSerializer(BaseModelSerializer):
    address = AddressSerializer(read_only=True)
    account = AccountSerializer(read_only=True)
    class Meta(BaseModelSerializer.Meta):
        model = Owner

class OwnerSaveSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Owner
        exclude = ['account', 'photo']

class OwnerSaveWithMiranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ['address','account', 'phone','photo',]
        
class OwnerSavePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['photo',]
        
    