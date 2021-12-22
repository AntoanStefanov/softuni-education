from django.urls import path
from . import views # . means current folder

urlpatterns = [
    # https://docs.djangoproject.com/en/4.0/intro/tutorial01/#path-argument-name
    path('', views.index, name="playground_index"),
    # always / at the end
    path('hello/', views.hello, name="playground_hello")

]

