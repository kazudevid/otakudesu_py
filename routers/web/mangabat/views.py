import controllers.mangabat as mangabat
from django.shortcuts import render

def index(request):
    mangas = mangabat.home(request)
    return render(request, 'mangabat/index.html', context=mangas)

def comic(request, endpoint):
    return render(request, 'mangabat/comic.html', context=mangabat.comic(request, endpoint))

def chapter(request, endpoint):
    return render(request, 'mangabat/chapter.html', context=mangabat.chapter(request, endpoint))

def search(request, query):
    return render(request, 'mangabat/search.html', context=mangabat.search(request, query))