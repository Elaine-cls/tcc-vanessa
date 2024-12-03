from django.shortcuts import render
from django.views import View

class CadastrarPetView(View):
    def get(self, request):
        return render(request, 'pages/cadastrar_pet.html')
