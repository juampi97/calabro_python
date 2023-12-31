from django.contrib import admin
from django.urls import path

from perfiles.views import registro, login_view, perfil_view, CustomLogoutView, MiPerfilUpdateView

urlpatterns = [
    path('signup/',registro,name="registro"),
    path('login/',login_view,name="login"),
    path('logout/',CustomLogoutView.as_view(),name="logout"),
    path('profile/',perfil_view,name="perfil"),
    path('editar-mi-perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
]