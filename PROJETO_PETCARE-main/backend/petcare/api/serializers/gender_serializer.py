from .base_serializer import BaseModelSerializer
from ...models import Gender

class GenderSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Gender