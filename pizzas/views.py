from django.shortcuts import render
from .models import Pizza, Topping
from .forms import ToppingForm

# Helper functions
def is_dupplicate(type, name):
    if type == "t":
        all_toppings = Topping.objects.all()
        for topping in all_toppings:
            if name.lower() == topping.name.lower():
                return True



def index(request):
    return render(request, 'pizzas/index.html')


# All views for owner's side (managing toppings)

def manage_toppings(request):
    return render(request, 'pizzas/toppings.html', {
        'toppings': Topping.objects.all()
    })

def add_topping(request):
    if request.method == 'POST':
        form = ToppingForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            if is_dupplicate(type="t", name=new_name):
                return render(request, 'pizzas/add_topping.html', {
                    'form': ToppingForm(),
                    'dup': True
                })
            else:
                new_topping = Topping(
                    name = new_name
                )
                new_topping.save()
                return render(request, 'pizzas/add_topping.html', {
                    'form': ToppingForm(),
                    'success': True
                })
    else:
        form = ToppingForm()
    return render(request, 'pizzas/add_topping.html', {
        'form': form
    })