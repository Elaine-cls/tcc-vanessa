from .base_vet_viewset import *
from ...serializers import VetSerializer, VetSaveSerializer

class VetViewSet(BaseVetAuthenticatedViewSet):
    def get_serializer_class(self):
        actions = {
            "me": VetSerializer
        }
        return actions.get(self.action, VetSaveSerializer)
    
    @action(detail=False, methods=['get'])
    def me(self,request):
        return Response(self.get_serializer(self.get_queryset()).data)