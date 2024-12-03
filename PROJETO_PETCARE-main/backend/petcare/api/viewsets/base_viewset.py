from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ...models import Owner

class BaseAuthenticatedViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def _get_user_authenticated(self):
        return self.request.user
    
    def _get_owner_authenticated(self):
        return Owner.objects.filter(account_id = self._get_user_authenticated().id).first()