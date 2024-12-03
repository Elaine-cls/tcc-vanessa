from django.shortcuts import render
from django.views import View

class PainelView(View):
    def get(self, request):
        return render(request, 'pages/painel.html')
