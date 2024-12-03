from .base_pet_viewset import BasePetAuthenticatedViewSet, action, Response
from ...serializers import MedicalHistorySerializer

class PetMedicalHistoryViewSet(BasePetAuthenticatedViewSet):
    def get_serializer_class(self):
        return MedicalHistorySerializer
    
    @action(detail=True, methods=['get'], url_path="medical-history")
    def medical_history(self, request, pk: None):
        serializer = self.get_serializer(self.get_queryset().filter(id = pk).first().medical_history)
        
        return Response(serializer.data)
    