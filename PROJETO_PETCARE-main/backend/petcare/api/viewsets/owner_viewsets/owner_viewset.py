from .base_owner_viewset import BaseOwnerAuthenticatedViewSet, mixins, Response, status, action
from ...serializers import OwnerSaveSerializer, OwnerSerializer, AddressSerializer, OwnerSavePhotoSerializer

class OwnerViewSet(BaseOwnerAuthenticatedViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    def get_serializer_class(self):
        actions = {
            "me": OwnerSerializer,
            "save_photo": OwnerSavePhotoSerializer
        }
        return actions.get(self.action, OwnerSaveSerializer)
    
    def create(self, request, *args, **kwargs):
        owner = self._get_owner_authenticated()
        if owner is not None:
            return Response({'error':'Already registered.'}, status.HTTP_406_NOT_ACCEPTABLE)
        
        address_data = request.data.get('address')
        serializer = self.get_serializer(data=request.data)
        address_serializer = AddressSerializer(data=address_data)          
    
        serializer.is_valid(raise_exception=True)
        address_serializer.is_valid(raise_exception=True)
        
        address_saved = address_serializer.save()
        
        owner_saved = serializer.save(account = self._get_user_authenticated(), address=address_saved)
        
        if owner_saved:
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk: None,*args, **kwargs):
        owner = self.get_queryset().filter(id=pk).first()
        if owner is None:
            return Response({'error':'Not Found.'}, status.HTTP_404_NOT_FOUND)
        address_data = request.data.get('address', {})
        address_serializer = AddressSerializer(data=address_data, instance=owner.address)
        owner_serializer = self.get_serializer(data=request.data, instance=owner)
        
        address_serializer.is_valid(raise_exception=True)
        owner_serializer.is_valid(raise_exception=True)
        
        address_saved = address_serializer.save()
        owner_serializer.save(address=address_saved)
        
        return Response(owner_serializer.data, status.HTTP_202_ACCEPTED)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        owner = self._get_owner_authenticated()
        if owner is None:
            return Response({'error':'not registered.'}, status.HTTP_400_BAD_REQUEST)
        return Response(self.get_serializer(owner).data)
    
    @action(detail=True, methods=['put'], url_path="save-photo")
    def save_photo(self, request, pk: None):
        owner = self.get_queryset().filter(id=pk).first()
        
        if owner is None:
            return Response({'error':'Not Found.'}, status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data, instance=owner)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        
        