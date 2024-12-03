from django.shortcuts import render
from django.views import View

class CadastrarContaView(View):
    def get(self, request):
        return render(request, 'pages/cadastrar_conta.html')
