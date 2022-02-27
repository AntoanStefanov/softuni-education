from django import forms

from app.models import Item, Profile


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.disable_fields = kwargs.pop('disable_fields', None)
        super().__init__(*args, **kwargs)

        if self.disable_fields:
            for field in self.fields:
                self.fields[field].disabled = True

        # Add STYLE
        # NOT SURE IF NEEDED, QUESTION IS IN LIBRARY NOTE, ASK DONCHO
        # self.fields['profile_image'].widget.attrs['style'] = 'form-file'

        # ADD PLACEHOLDERS
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['age'].widget.attrs['placeholder'] = 'Age'

        # remove ":" in labels
        # self.label_suffix = ""
    
    class Meta:
        model = Profile

        # IF ORDER IS NEEDED, DO IT BELOW
        fields = ['username', 'email', 'age']

        # labels = {
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'profile_image': 'Profile Image'
        # }
        # exclude = ('field1','field2')


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.disable_fields = kwargs.pop('disable_fields', None)

        super().__init__(*args, **kwargs)

        if self.disable_fields:
            for field in self.fields:
                self.fields[field].disabled = True

        self.fields['album_name'].widget.attrs['placeholder'] = 'Album Name'
        self.fields['artist'].widget.attrs['placeholder'] = 'Artist'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['image'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'

        # remove ":" in labels
        # self.label_suffix = ""

    class Meta:
        model = Item
        fields = ['album_name', 'artist', 'genre', 'description', 'image', 'price']
        labels = {
            'album_name': 'Album Name',
            'image': 'Image URL',
        }
