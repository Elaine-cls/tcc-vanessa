from django.shortcuts import render
from django.views import View

class CadastrarClinicaVetView(View):
    def get(self, request):
        return render(request, 'pages/cadastrar_clinica.html')
