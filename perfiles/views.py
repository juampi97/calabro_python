from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import UpdateView

from perfiles.forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )

@login_required
def perfil_view(request):
         contexto = {
         }
         http_response = render(
             request=request,
             template_name='perfiles/perfil_view.html',
             context=contexto,
         )
         return http_response

class CustomLogoutView(LoginRequiredMixin,LogoutView):
   template_name = 'perfiles/logout.html'

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('perfil')
   template_name = 'perfiles/formulario_perfil.html'

   def get_object(self, queryset=None):
       return self.request.user