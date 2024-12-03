from .base_serializer import BaseModelSerializer
from ...models import Address

class AddressSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Address