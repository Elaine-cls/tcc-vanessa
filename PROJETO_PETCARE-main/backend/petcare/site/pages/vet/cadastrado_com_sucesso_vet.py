from django.shortcuts import render
from django.views import View

class CadastradoComSucessoVetView(View):
    def get(self, request):
        return render(request, 'pages/clinica_cadastrada.html')
