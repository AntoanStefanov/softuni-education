from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RecipeForm
from .models import Recipe


def index(request):
    recipes = list(Recipe.objects.all())
    return render(request, 'index.html', {'recipes': recipes})


def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe = Recipe()
            recipe.title = data['title']
            recipe.image_url = data['imageURL']
            recipe.description = data['description']
            recipe.ingredients = data['ingredients']
            recipe.time = data['time']
            recipe.save()

            return HttpResponseRedirect('/')
    else:
        form = RecipeForm()

    return render(request, 'create.html', {'form': form})


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return HttpResponseRedirect('/')
    else:
        initial = {
            'title': recipe.title,
            'imageURL': recipe.image_url,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'time': recipe.time
        }

        form = RecipeForm(initial=initial)

        for fieldname in form.fields:
            form.fields[fieldname].disabled = True

    return render(request, 'delete.html', {'form': form})


def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    return render(request, 'details.html', {'recipe': recipe})


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            recipe.title = data['title']
            recipe.image_url = data['imageURL']
            recipe.description = data['description']
            recipe.ingredients = data['ingredients']
            recipe.time = data['time']
            recipe.save()

            return HttpResponseRedirect('/')
    else:
        initial = {
            'title': recipe.title,
            'imageURL': recipe.image_url,
            'description': recipe.description,
            'ingredients': recipe.ingredients,
            'time': recipe.time
        }

        form = RecipeForm(initial=initial)

    return render(request, 'edit.html', {'form': form})
