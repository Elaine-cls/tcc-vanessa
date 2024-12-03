from ..base_viewset import *
from ....models import Pet

class BasePetAuthenticatedViewSet(BaseAuthenticatedViewSet):
    def get_queryset(self):
        return Pet.objects.filter(owner__account_id = self.request.user.id)