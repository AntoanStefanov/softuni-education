from django.shortcuts import get_object_or_404, redirect, render

from app.forms import NoteForm, RegisterForm
from app.models import Note, Profile


def index(request):
    profile = Profile.objects.first()

    if profile:
        notes = Note.objects.all()
        return render(request, 'home-with-profile.html', {'notes': notes})
    else:
        # https://docs.djangoproject.com/en/4.0/topics/forms/#the-view - view with form in it.
        if request.method == 'POST':
            # create a form instance and populate it with data from the request.
            form = RegisterForm(request.POST)
            if form.is_valid():
                # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/#the-save-method - save method
                form.save()
                return redirect('index')
        else:
            # if a GET (or any other method) create a blank form.
            form = RegisterForm()

        return render(request, 'home-no-profile.html', {'form': form})


def add_note(request):
    if request.method == 'POST':
        # Create a form instance from POST data.
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save a new object from the form's data.
            form.save()
            return redirect('index')
    else:
        form = NoteForm()

    return render(request, 'note-create.html', {'form': form})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)

    return render(request, 'note-edit.html', {'form': form})


def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        form = NoteForm(instance=note, disable_fields=True)

    return render(request, 'note-delete.html', {'form': form})


def details_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, 'note-details.html', {'note': note})


def profile(request):
    if request.method == 'POST':
        Profile.objects.first().delete()
        Note.objects.all().delete()

        return redirect('index')
    else:
        profile = Profile.objects.first()
        number_of_notes = Note.objects.count()

        context = {'profile': profile, 'number_of_notes': number_of_notes}

        return render(request, 'profile.html', context)
