from ..base_viewset import *
from ...permissions import IsVet
from ....models import Vet

class BaseVetAuthenticatedViewSet(BaseAuthenticatedViewSet):
    permission_classes = [IsVet]
    
    def _get_vet_authenticated(self):
        return Vet.objects.filter(account = self._get_user_authenticated()).first()
    
    def get_queryset(self):
        return self._get_vet_authenticated()