from django import forms
from .models import AnimalFood


class AnimalFoodForm(forms.ModelForm):
    name = forms.ImageField()
    food = forms.ImageField()
    class Meta():
        model=AnimalFood
        fields=['name','food']

