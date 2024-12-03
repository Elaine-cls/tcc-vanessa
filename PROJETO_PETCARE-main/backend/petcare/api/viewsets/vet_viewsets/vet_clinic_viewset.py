from .base_vet_viewset import *
from ....models import Clinic
from ...serializers import ClinicSerializer, AddressSerializer

class VetClinicViewSet(BaseVetAuthenticatedViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    def get_serializer_class(self):
        return ClinicSerializer
    
    def get_queryset(self):
        return Clinic.objects.filter(id = self._get_vet_authenticated().clinic.id)
    
    def update(self, request, *args, **kwargs):
        address_data = request.data.get('address', {})
        address_serializer = AddressSerializer(data=address_data, instance=self.get_queryset().first().address)
        clinic_serializer = self.get_serializer(data=request.data, instance=self.get_queryset().first())
        
        address_serializer.is_valid(raise_exception=True)
        clinic_serializer.is_valid(raise_exception=True)
        
        address_saved = address_serializer.save()
        clinic_serializer.save(address = address_saved)
        
        return Response(clinic_serializer.data, status.HTTP_202_ACCEPTED)
    
    