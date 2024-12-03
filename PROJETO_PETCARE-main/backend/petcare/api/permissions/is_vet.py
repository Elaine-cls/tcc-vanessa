from .base_permissions import *
from ...models import Vet

class IsVet(BasePermission):
    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado e vinculado a um cadastro de Vet
        return request.user.is_authenticated and Vet.objects.filter(account=request.user).exists()