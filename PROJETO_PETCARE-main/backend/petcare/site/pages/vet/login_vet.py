from django.shortcuts import render
from django.views import View

class LoginVetView(View):
    def get(self, request):
        return render(request, 'pages/login_veterinario.html')
