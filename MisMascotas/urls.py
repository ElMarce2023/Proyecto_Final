"""
URL configuration for Mascotas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import MascotasView
from .views import ConsumirAPIView
from .views import Form1View
from .views import NosotrosView
from .views import NoticiasView




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MascotasView.as_view(), name = "index"),
    path("consumirAPI/", ConsumirAPIView.as_view(), name = "consumirAPI"),
    path("form1/", Form1View.as_view(), name = "form1"),
    path("nosotros/", NosotrosView.as_view(), name = "nosotros"),
    path("noticias/", NoticiasView.as_view(), name = "noticias"),
    
    

]
