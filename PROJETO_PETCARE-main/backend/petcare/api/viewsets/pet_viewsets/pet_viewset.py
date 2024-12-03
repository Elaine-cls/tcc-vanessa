from .base_pet_viewset import BasePetAuthenticatedViewSet, mixins, Response, status
from ...serializers import PetSerializer, PetSaveSerializer, PetDetailSerializer
from ....models import MedicalHistory

class PetViewSet(BasePetAuthenticatedViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    def get_serializer_class(self):
        actions = {
            "list": PetSerializer,
            "retrieve": PetDetailSerializer
        }
        return actions.get(self.action, PetSaveSerializer)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        medical_history = MedicalHistory.objects.create()
        
        pet_saved = serializer.save(owner = self._get_owner_authenticated(), medical_history = medical_history)
        
        if pet_saved:
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        
    
    