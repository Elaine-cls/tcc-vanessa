from .base_vet_viewset import *
from ....models import Pet, Medicine, Illness, Surgery, Consultation
from ...serializers import PetDetailSerializer, MedicineSaveSerializer, IllnessSaveSerializer, SurgerySaveSerializer, ConsultationSaveSerializer


class VetPetBaseVewSet(BaseVetAuthenticatedViewSet):
    def get_queryset(self):
        return Pet.objects.all()

class VetPetViewSet(VetPetBaseVewSet, mixins.RetrieveModelMixin):
     
    def get_serializer_class(self):
        return PetDetailSerializer
    
class VetPetMedicalHistoryViewSet(VetPetBaseVewSet):
     
    def get_serializer_class(self):
        actions = {
            "add_medicine": MedicineSaveSerializer,
            "add_illness": IllnessSaveSerializer,
            "add_surgery": SurgerySaveSerializer,
            "add_consultation": ConsultationSaveSerializer
        }
        return actions.get(self.action, MedicineSaveSerializer)
    
    def __save_info_on_medical_history(self, request, pk:None):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        pet = self.get_queryset().filter(id = pk).first()
        if pet is None:
            return Response('Pet not found.')
        
        data = serializer.save(medical_history = pet.medical_history)
        
        if data:
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'], url_path="medicine/add")
    def add_medicine(self, request, pk: None):
        return self.__save_info_on_medical_history(request, pk)
    
    @action(detail=True, methods=['post'], url_path="illness/add")
    def add_illness(self, request, pk: None):
        return self.__save_info_on_medical_history(request, pk)
        
    @action(detail=True, methods=['post'], url_path="surgery/add")
    def add_surgery(self, request, pk:None):
        return self.__save_info_on_medical_history(request, pk)
    
    @action(detail=True, methods=['post'], url_path="consultation/add")
    def add_consultation(self, request, pk:None):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        current_vet = self._get_vet_authenticated()
        pet = self.get_queryset().filter(id = pk).first()
        if pet is None:
            return Response('Pet not found.')
        data = serializer.save(medical_history = pet.medical_history, vet = current_vet, clinic = current_vet.clinic)
        
        if data:
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class VetPetMedicineDetailsViewSet(VetPetBaseVewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return MedicineSaveSerializer
    
    def get_queryset(self):
        return Medicine
    
class VetPetIllnessDetailsViewSet(VetPetBaseVewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return IllnessSaveSerializer
    
    def get_queryset(self):
        return Illness
    
class VetPetSurgeryDetailsViewSet(VetPetBaseVewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return SurgerySaveSerializer
    
    def get_queryset(self):
        return Surgery
    
class VetPetConsultationDetailsViewSet(VetPetBaseVewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    def get_serializer_class(self):
        return ConsultationSaveSerializer
    
    def get_queryset(self):
        return Consultation


    