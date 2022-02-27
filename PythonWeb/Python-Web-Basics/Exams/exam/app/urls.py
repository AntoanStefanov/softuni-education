from django.urls import path

from app.views import (add_item, delete_item, delete_profile, details_item,
                       edit_item, index, profile)

urlpatterns = [
    path('', index, name='index'),
    path('album/add/', add_item, name='create-item'),
    path('album/details/<int:pk>/', details_item, name='details-item'),
    path('album/edit/<int:pk>/', edit_item, name='edit-item'),
    path('album/delete/<int:pk>/', delete_item, name='delete-item'),
    path('profile/details/', profile, name='profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),
]
