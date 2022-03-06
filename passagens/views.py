from django.shortcuts import render
from passagens.forms import PassagensForms


def index(request):
    form = PassagensForms()
    contexto = {
        'form': form
    }
    return render(request, 'index.html', contexto)
