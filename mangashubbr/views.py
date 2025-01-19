from django.shortcuts import render

def index(request):
    return render(request, 'mangashubbr/index.html')

def imagem(request):
    return render(request, 'mangashubbr/imagem.html')