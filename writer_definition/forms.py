from django import forms

from .models import WriterDefinition


class WriterDefinitionForm(forms.ModelForm):
    class Meta:
        model = WriterDefinition
        fields = ('writerName','host','dbName','username','password')
