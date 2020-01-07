from django import forms

from .models import ReaderDefinition


class ReaderDefinitionForm(forms.ModelForm):
    class Meta:
        model = ReaderDefinition
        fields = ('readerName', 'path', 'type',)
