from .base_serializer import *
from ...models import SurgeryStatus, Surgery

class SurgeryStatusSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = SurgeryStatus
        
        
class SurgerySerializer(BaseModelExcludeSerializer):
    surgery_status = SurgeryStatusSerializer(read_only=True)
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Surgery
        
class SurgerySaveSerializer(BaseModelSerializer):
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Surgery