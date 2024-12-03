from .base_viewset import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AccountAuthenticatedViewSet(viewsets.ViewSet, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            # Obtém o token do usuário autenticado
            token = request.auth
            if token:
                token.delete()  # Remove o token
                return Response({'success': 'Logout realizado com sucesso.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Nenhum token encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['get'])
    def me(self, request):
        # Retorna as informações do usuário autenticado
        user = request.user
        data = {
            "username": user.username,
            "email": user.email
        }
        return Response(data, status=status.HTTP_200_OK)