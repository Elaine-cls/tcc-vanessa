from ..base_viewset import *
import requests
from django.conf import settings
from ...serializers import OwnerSaveWithMiranteSerializer, AddressSerializer

class MiranteViewSet(BaseAuthenticatedViewSet, viewsets.ViewSet):    
    serializer_class = OwnerSaveWithMiranteSerializer
    @action(detail=False, methods=['post'], url_path="create-with-mirante")
    def create_with_mirante(self, request):
        try:
            # Obter o token de autenticação
            token = self.__get_token()
            
            # Buscar dados do Mirante
            data_mirante = self.__find_data_on_mirante(token)
            if not data_mirante:
                return Response({"error": "Falha ao obter dados do Mirante."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Buscar endereço pelo CEP
            vipcep = self.__request_to_cep(data_mirante.get('cep'))
            if not vipcep:
                return Response({"error": "CEP inválido ou não encontrado."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Preparar dados para o AddressSerializer
            address_data = {
                "cep": vipcep.get("cep", "").replace('-', ''),
                "street": vipcep.get("logradouro", ""),
                "city": vipcep.get("localidade", ""),
                "state": vipcep.get("uf", ""),
                "country": "Brasil",
            }
            
            address_serializer = AddressSerializer(data=address_data)
            serializer = OwnerSaveWithMiranteSerializer(data=data_mirante)

            # Validar serializers
            address_serializer.is_valid(raise_exception=True)
            serializer.is_valid(raise_exception=True)

            # Salvar endereço e dados do Mirante
            address_saved = address_serializer.save()
            saved = serializer.save(address=address_saved, account=self._get_user_authenticated())
            
            if saved:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "Falha ao salvar dados."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        except (ValueError, TimeoutError) as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Erro inesperado: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def __get_token(self):
        data = {
            "email":settings.MIRANTE_CREDENTIALS_LOGIN_EMAIL,
            "password":settings.MIRANTE_CREDENTIALS_LOGIN_PASSWORD
        }

        response = self.__request_post(settings.MIRANTE_AUTHENTICATE, data, {})
        
        if isinstance(response, dict) and response.get('token'):
            return response.get('token')
        raise ValueError("Falha ao autenticar com o Mirante. Verifique as credencias.")
       
    
    def __find_data_on_mirante(self, token):
        
        if not token:
            raise ValueError("Token invalido ou ausente.")
        
        data = {
            "user_email":self.request.user.email
        }
        url = settings.MIRATE_ROUTE_USERS
        headers = {'Authorization':f'Bearer {token}'}

        response = self.__request_post(url, data, headers)
        
        if isinstance(response, dict):
            user_data = response.get('user')
            if user_data:
                return user_data
            raise ValueError("Dados do usuário não encontrados na resposta.")
        raise ValueError(f"Resposta inválida recebida: {response}")
    
    def __request_post(self, url, data, headers):
        try:
            response = requests.post(url, json=data, headers=headers, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise TimeoutError("A requisição excedeu o tempo limite!")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Ocorreu um erro na requisição: {e}")
            
        
    
    def __request_to_cep(self, cep):
        if not cep or not cep.isdigit() or len(cep) != 8:
            raise ValueError("CEP inválido fornecido.")
        
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if "erro" in data:
                raise ValueError(f"CEP não encontrado: {cep}")
            return data
        except requests.exceptions.Timeout:
            raise TimeoutError("A requisição para o serviço de CEP excedeu o tempo limite.")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Erro ao buscar dados do CEP: {e}")




    
