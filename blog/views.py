from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Articulo
# from blog.forms import ArticuloForm, ComentarioForm

# Create your views here.

class PostListView(ListView):
    model = Articulo
    template_name = 'blog/articulos_lista.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

# class PostCreateView(CreateView):
#     model = Articulo
#     fields = ('titulo', 'subtitulo', 'categoria', 'autor', 'cuerpo')
#     success_url = reverse_lazy('blog')

# class PostUpdateView(UpdateView):
#     model = Articulo
#     fields = ('titulo', 'subtitulo', 'categoria', 'autor', 'cuerpo')
#     success_url = reverse_lazy('blog')
# class PostDeleteView(DeleteView):
#     model = Articulo
#     success_url = reverse_lazy('blog')