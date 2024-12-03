from django.shortcuts import render
from django.views import View

class BemVindoView(View):
    def get(self, request):
        # Lógica para processar a requisição GET (por exemplo, renderizar um template)
        return render(request, 'pages/bem_vindo.html')
