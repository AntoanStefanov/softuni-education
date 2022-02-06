from django import forms


class RecipeForm(forms.Form):
    #  disabled = True tuk moje da gi disable-nesh
    title = forms.CharField(label='Title', max_length=30)
    imageURL = forms.URLField(label='Image URL')
    description = forms.CharField(label='Description', widget=forms.Textarea)
    ingredients = forms.CharField(label='Ingredients', max_length=250)
    time = forms.IntegerField(label='Time (Minutes)')
