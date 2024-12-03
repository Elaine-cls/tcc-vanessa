from .base_serializer import *
from ...models import MedicalHistory
from .medicine_serializer import MedicineSerializer
from .illness_serializer import IllnessSerializer
from .surgery_serializer import SurgerySerializer
from .consultation_serializer import ConsultationSerializer

class MedicalHistorySerializer(BaseModelSerializer):
    medicines = MedicineSerializer(read_only=True, many=True)
    illnesses = IllnessSerializer(read_only=True, many=True)
    surgeries = SurgerySerializer(read_only=True, many=True)
    queries = ConsultationSerializer(read_only=True, many=True)
    
    class Meta(BaseModelSerializer.Meta):
        model = MedicalHistory