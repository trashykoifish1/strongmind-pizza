from django import forms
from .models import Pizza, Topping

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {
            'name': 'Topping Type',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }