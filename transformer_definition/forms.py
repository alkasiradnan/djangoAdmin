from django import forms

from .models import TransformerDefinition


class TransformerDefinitionForm(forms.ModelForm):
    class Meta:
        model = TransformerDefinition
        fields = ('transformerName', 'path',)
