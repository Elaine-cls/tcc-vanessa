from django.shortcuts import render
from django.views import View
from django.conf import settings
import requests

class InicioView(View):
    def get(self, request):
        # Lógica para processar a requisição GET (por exemplo, renderizar um template)
        return render(request, 'pages/inicio.html')
