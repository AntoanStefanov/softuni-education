from django.urls import path

from app.views import (add_note, delete_note, details_note, edit_note, index,
                       profile)

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add-note'),
    path('edit/<int:pk>', edit_note, name='edit-note'),
    path('delete/<int:pk>', delete_note, name='delete-note'),
    path('details/<int:pk>', details_note, name='details-note'),
    path('profile/', profile, name='profile'),
]
