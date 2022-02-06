from django import forms

from app.models import Note, Profile


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove ":" in labels
        self.label_suffix = ""

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'image_url')
        labels = {
            'image_url': 'Link to Profile Image'
        }
        # exclude = ('field1','field2')


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.disable_fields = kwargs.pop('disable_fields', None)
        super().__init__(*args, **kwargs)

        if self.disable_fields:
            for field in self.fields:
                self.fields[field].disabled = True
        # remove ":" in labels
        self.label_suffix = ""

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')
        labels = {
            'image_url': 'Link to Image'
        }
