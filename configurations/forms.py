from django import forms

from .models import Configuration


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = ('configurationName','reader','transformer','writer')
