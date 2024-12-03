from django.shortcuts import render
from django.views import View

class PetsView(View):
    def get(self, request):
        return render(request, 'pages/pets.html')
