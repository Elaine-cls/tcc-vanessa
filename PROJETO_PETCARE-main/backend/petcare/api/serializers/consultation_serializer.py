from .base_serializer import *
from ...models import Consultation
from .vet_serializer import VetSerializer
from .clinic_serializer import ClinicSerializer

class ConsultationSerializer(BaseModelExcludeSerializer):
    vet = VetSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Consultation

class ConsultationSaveSerializer(BaseModelExcludeSerializer):
    class Meta(BaseModelExcludeSerializer.Meta):
        model = Consultation
        exclude = ('medical_history','vet','clinic')