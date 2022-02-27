import os

from django.shortcuts import get_object_or_404, redirect, render

from app.forms import ItemForm, ProfileForm
from app.models import Item, Profile


def index(request):
    profile = Profile.objects.first()

    if profile:
        albums = Item.objects.all()

        context = {
            'albums': albums,
        }

        return render(request, 'home-with-profile.html', context)
    else:
        # https://docs.djangoproject.com/en/4.0/topics/forms/#the-view - view with form in it.
        if request.method == 'POST':
            # create a form instance and populate it with data from the request.
            form = ProfileForm(request.POST, request.FILES)

            if form.is_valid():
                # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#the-save-method - save method
                form.save()
                return redirect('index')
        else:
            # if a GET (or any other method) create a blank form.
            form = ProfileForm()

        return render(request, 'home-no-profile.html', {'form': form})


def add_item(request):
    if request.method == 'POST':
        # Create a form instance from POST data.
        form = ItemForm(request.POST)
        if form.is_valid():
            # Save a new object from the form's data.
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    return render(request, 'add-album.html', {'form': form})


def edit_item(request, pk):
    album = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm(instance=album)

    return render(request, 'edit-album.html', {'form': form})


def details_item(request, pk):
    album = get_object_or_404(Item, pk=pk)

    return render(request, 'album-details.html', {'album': album})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    else:
        form = ItemForm(instance=item, disable_fields=True)

    return render(request, 'delete-album.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        Profile.objects.first().delete()
        Item.objects.all().delete()

        return redirect('index')
    else:
        profile = Profile.objects.first()
        albums = Item.objects.all()
        context = {
            'profile': profile,
            'number_of_albums': len(albums),
        }

        return render(request, 'profile-details.html', context)


# def edit_profile(request):
#     profile = Profile.objects.first()

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'profile-edit.html', {'form': form})


def delete_profile(request):
    if request.method == 'POST':
        Profile.objects.first().delete()
        Item.objects.all().delete()

        return redirect('index')

    return render(request, 'profile-delete.html')
