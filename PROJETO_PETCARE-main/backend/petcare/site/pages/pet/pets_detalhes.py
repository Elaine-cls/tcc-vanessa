from django.shortcuts import render
from django.views import View

class PetsDetailsView(View):
    def get(self, request, id):
        return render(request, 'pages/pet_details.html', {'pet': ''})
