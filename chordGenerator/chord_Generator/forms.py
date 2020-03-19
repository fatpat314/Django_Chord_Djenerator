from django import forms
from chord_Generator import Chords


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta():
        model = Chords
        fields = ['amount']
