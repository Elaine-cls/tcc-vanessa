from django.shortcuts import render
from django.views import View

class CadastradoComSucessoView(View):
    def get(self, request):
        return render(request, 'pages/cadastrado_com_sucesso.html')
