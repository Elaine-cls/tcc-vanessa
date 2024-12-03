"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, permissions
from petcare.views import route as routepetcare
from petcare.site.urls import urlpatterns as petcaresiteurls

from authentication.api import viewsets as authenticationviewsets 

route = routers.DefaultRouter()

route.register(r'accounts', authenticationviewsets.AccountNotAuthenticatedViewSet, basename="account-notauthenticated")
route.register(r'accounts', authenticationviewsets.AccountAuthenticatedViewSet, basename="account-authenticated")



schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(petcaresiteurls)),
    path('', include(route.urls)),
    path('', include(routepetcare.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
