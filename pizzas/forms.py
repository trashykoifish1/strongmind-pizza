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

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields = ['name', 'toppings']
        labels = {
            'name': 'Pizza Name',
            'toppings': 'Toppings',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    toppings = forms.ModelMultipleChoiceField(
        queryset = Topping.objects.all(),
        widget = forms.SelectMultiple(attrs={
            'class': 'form-control'
        })
    )
