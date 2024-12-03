from ..base_viewset import *
from ...serializers import ClinicAndVetSaveSerializer, AccountCreateSerializer, VetSaveSerializer, AddressSerializer

class ClinicNotAuthenticatedViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    def get_serializer_class(self):
        return ClinicAndVetSaveSerializer
    
    def create(self, request, *args, **kwargs):
        vet_data = request.data.get('vet', {})
        account_data = vet_data.get('account',{})
        address_data = request.data.get('address', {})
        
        vet_serializer = VetSaveSerializer(data=vet_data)
        account_serializer = AccountCreateSerializer(data=account_data)
        address_serializer = AddressSerializer(data=address_data)
        clinic_serializer = self.get_serializer(data=request.data)
        
        
        account_serializer.is_valid(raise_exception=True)
        vet_serializer.is_valid(raise_exception=True)
        address_serializer.is_valid(raise_exception=True)
        clinic_serializer.is_valid(raise_exception=True)        
        
        account_saved = account_serializer.save()
        address_saved = address_serializer.save()
        clinic_saved = clinic_serializer.save(address=address_saved)
        vet_serializer.save(clinic = clinic_saved, account=account_saved)
        

        return Response(clinic_serializer.data, status.HTTP_201_CREATED)