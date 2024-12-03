from .base_viewset import *

from ..serializers import AccountCreateSerializer, AccountLoginSerializer

class AccountNotAuthenticatedViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def get_serializer_class(self):
        action_serializers = {
            "login": AccountLoginSerializer,
        }
        return action_serializers.get(self.action, AccountCreateSerializer)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
            
        # Autentica o usuário
        user = authenticate(request, email=email, password=password)
            
        if user is not None:
            # Se as credenciais estão corretas, obtenha ou crie o token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)