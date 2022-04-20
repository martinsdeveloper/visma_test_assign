from email.policy import default
from django import forms
from .models import SearchRecord
from django.utils.translation import gettext as _

class SearchRecordCreateForm(forms.ModelForm):
    class Meta:
        model = SearchRecord
        fields = ('url', 'keywords', 'count_of_matches')
        widgets = {'url':  forms.TextInput(), 'keywords': forms.TextInput(), 'count_of_matches': forms.HiddenInput( attrs={ 'value': '0' } )}
