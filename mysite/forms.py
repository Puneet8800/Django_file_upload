from django import forms

from .models import upload


class upload_form(forms.ModelForm):
    class Meta:
        model = upload
        fields = ('name', 'description', 'pdf')
    