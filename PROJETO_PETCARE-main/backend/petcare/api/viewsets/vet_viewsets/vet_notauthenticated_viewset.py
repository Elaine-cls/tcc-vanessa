from ..base_viewset import *
from authentication.api.serializers import AccountLoginSerializer
from authentication.api.viewsets.base_viewset import authenticate, Token
from ....models import Vet

class VetNotAuthenticatedViewSet(viewsets.GenericViewSet):
    
    def get_serializer_class(self):
        return AccountLoginSerializer
    
    def get_queryset(self):
        return Vet.objects.all()
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
            
        # Autentica o usuário
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            vet = self.get_queryset().filter(account = user).first()
            
            # Se existe um veterinario com essa conta depois obtenha ou crie o token
            if vet:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    