from ..base_viewset import *
from ....models.owner import Owner

class BaseOwnerAuthenticatedViewSet(BaseAuthenticatedViewSet):
    
    def _get_owner_authenticated(self):
        return Owner.objects.filter(account_id = self._get_user_authenticated().id).first()
    
    def get_queryset(self):
        user = self._get_user_authenticated()
        return Owner.objects.filter(account=user)
    