from .models import AudioBook
from django import forms


class AudioBookForm(forms.ModelForm):
    class Meta:
        model = AudioBook
        fields = (
            'title',
            'author',
            'narrator',
            'duration',
        )
        labels = {
            'title': 'Title',
            'author': 'Author',
            'narrator': 'Narrator',
            'duration': 'Duration',
        }
