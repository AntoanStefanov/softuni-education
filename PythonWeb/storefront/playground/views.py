from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Here we define our views.
# A view function takes a request and return a response.
# A view function is a request handler.
# A view in other frameworks here in Django is called a template.
# Here view means request handler / action in other frameworks


def index(request):
    # We can do everything in this function,
    # pull data from database,
    # transform data,
    # send emails and so on.

    return HttpResponse("Hello, world. You're at the playground index.")

    # We need to map this view function to a URL,
    # so when we get a request at that URL,
    # this function will be called


def hello(request):

    #  sudo fuser -k 8000/tcp. This should kill all the processes associated with port 8000.

    # render returns http response
    return render(request, 'hello.html', {'name': 'Tony'})
