from .base_serializer import *
from ...models import MedicineType, Medicine

class MedicineTypeSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = MedicineType

class MedicineSerializer(BaseModelExcludeSerializer):
    medicine_type = MedicineTypeSerializer(read_only=True)
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Medicine

class MedicineSaveSerializer(BaseModelExcludeSerializer):
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Medicine