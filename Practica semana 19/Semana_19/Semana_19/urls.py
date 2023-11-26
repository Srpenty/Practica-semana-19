"""
URL configuration for Semana_19 project.

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
from Practica_Sem_19 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('registro/',views.reg_user,name='registrarse'),
    path('login/',views.iniciar_sesion,name='login'),
    path('logout/',views.cerrar_session,name='logout'),
    path('addProveedores/',views.vAddProveedores,name='addProveedores'),
    path('addProductos/',views.vAddProductos,name='addProductos'),
    path('listProveedores/',views.vProveedores,name='listProveedores'),
    path('listProductos/',views.vProductos,name='listProductos'),
]
