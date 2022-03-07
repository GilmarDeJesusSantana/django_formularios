from django.shortcuts import render
from passagens.forms import PassagensForms


def index(request):
    form = PassagensForms()

    contexto = {
        'form': form
    }
    return render(request, 'index.html', contexto)


def consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        if form.is_valid():
            contexto = {
                'form': form
            }
            return render(request, 'consulta.html', contexto)
        else:
            print('Form inválido')
            contexto = {
                'form': form
            }
            return render(request, 'index.html', contexto)
