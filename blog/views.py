from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from blog.models import Articulo
from blog.forms import ArticuloPostForm

# Create your views here.
class PostListView(ListView):
    model = Articulo
    template_name = 'blog/articulos_lista.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloPostForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloPostForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('blog')

class PostDetailView(DetailView):
   model = Articulo
   success_url = reverse_lazy('blog')

@login_required
def PostFilterByAutor(request):
    articulos = Articulo.objects.filter(autor=request.user)
    contexto = {
            "articulos": articulos,
            "cantidad": articulos.count()
    }
    http_response = render(
        request=request,
        template_name='blog/articulos_lista_usuario.html',
        context=contexto,
    )
    return http_response

class PostUpdateView(LoginRequiredMixin, UpdateView):
     model = Articulo
     fields = ('titulo', 'subtitulo', 'categoria', 'cuerpo')
     success_url = reverse_lazy('mis-posts')

class PostDeleteView(LoginRequiredMixin, DeleteView):
     model = Articulo
     success_url = reverse_lazy('mis-posts')