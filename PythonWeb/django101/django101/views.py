from django.shortcuts import render


def index(request):
    context = {
        'name': 'Tony'
    }
    return render(request, 'index.html')
