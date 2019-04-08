from django import forms
from .models import Snack, Store


class CreateSnack(forms.ModelForm):
    class Meta:
        model = Snack
        exclude = ['date_found', 'author']


class CreateStore(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
