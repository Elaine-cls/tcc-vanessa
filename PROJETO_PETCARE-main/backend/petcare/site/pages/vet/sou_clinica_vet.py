from django.shortcuts import render
from django.views import View

class SouClinicaVetView(View):
    def get(self, request):
        return render(request, 'pages/sou_clinica.html')
