from .base_serializer import *
from ...models import IllnessStatus, Illness

class IllnessStatusSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = IllnessStatus
        
        
class IllnessSerializer(BaseModelExcludeSerializer):
    illness_status = IllnessStatusSerializer(read_only=True)
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Illness
        
class IllnessSaveSerializer(BaseModelExcludeSerializer):
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Illness