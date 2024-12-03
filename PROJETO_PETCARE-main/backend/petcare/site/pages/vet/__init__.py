from .cadastrar_vet import CadastrarClinicaVetView
from .login_vet import LoginVetView
from .sou_clinica_vet import SouClinicaVetView
from .painel import PainelView
from .cadastrado_com_sucesso_vet import CadastradoComSucessoVetView

# views.py
from django.shortcuts import render

prefix = 'pages'

def pesquisar_por_um_pet(request):
    return render(request, f'{prefix}/pesquisar-pet-vet.html')

def pesquisar_por_um_pet_id(request, id):
    return render(request, f'{prefix}/pesquisar-pet-vet.html', {'pet': ''})