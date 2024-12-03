from .base_serializer import *
from ...models import Pet
from .gender_serializer import GenderSerializer
from .owner_serializer import OwnerSerializer
from .medical_history_serializer import MedicalHistorySerializer

class PetSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ('medical_history', 'owner')

class PetDetailSerializer(BaseModelSerializer):
    gender = GenderSerializer(read_only=True)
    owner = OwnerSerializer(read_only=True)
    medical_history = MedicalHistorySerializer(read_only=True)
    class Meta(BaseModelSerializer.Meta):
        model = Pet
        
class PetSerializer(BaseModelSerializer):
    gender = GenderSerializer(read_only=True)
    class Meta(BaseModelSerializer.Meta):
        model = Pet