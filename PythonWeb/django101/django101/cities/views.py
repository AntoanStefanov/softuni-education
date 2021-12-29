from django.shortcuts import render

from django101.cities.models import Person


def index(request):
    context = {
        'name': 'Tony',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)
