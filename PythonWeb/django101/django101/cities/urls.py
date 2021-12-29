from django.urls import path

from django101.cities.views import index, phone_list

urlpatterns = [
    path('', index),
    path('phones/', phone_list),
]
