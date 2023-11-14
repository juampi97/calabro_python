from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'inicio.html',
        context = contexto,
    )
    return http_response

def about(request):
    contexto = {}
    http_response = render(
        request = request,
        template_name = 'about.html',
        context = contexto,
    )
    return http_response