from django.http import HttpResponse
from django.shortcuts import render

from django101.cities.models import Person


def index(request):
    context = {
        'name': 'Tony',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)


def phone_list(request):
    return HttpResponse('Phone list')
