from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Pizza, Topping
from .forms import ToppingForm, PizzaForm

# Helper functions

def is_dupplicate(type:str, name:str) -> bool:
    """
    type: "t" or "p" (toppings or pizzas)
    name: topping name or pizza name
    --------
    This function only checks for the duplicate name
    """
    if type == "t": # Check topping duplicates
        all_toppings = Topping.objects.all()
        for topping in all_toppings:
            if name.lower() == topping.name.lower():
                return True
    if type == "p": # Check pizza duplicates

        all_pizzas = Pizza.objects.exclude(name=name)
        for pizza in all_pizzas:
            if name.lower() == pizza.name.lower():
                return True

# def has_same_toppings(toppings, pizza = None) -> bool:
#     """
#     This function takes in a toppings QuerrySet, and check if it is a duplicate or not
#     """
#     print(pizza.name)
#     all_pizzas = Pizza.objects.exclude(name=pizza.name)
#     print(all_pizzas)
#     for pizza in all_pizzas:
#         print(pizza.name)
#         if set(pizza.toppings.all()) == set(toppings):
#             print(pizza.toppings.all())
#             print(toppings)
#             return True


# Landing page
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
            new_name = form.cleaned_data['name'].title()
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

def update_topping(request, id):
    if request.method == "POST":
        topping = Topping.objects.get(pk=id)
        form = ToppingForm(request.POST, instance=topping)
        if form.is_valid():
            if is_dupplicate(type="t", name=form.cleaned_data['name']):
                return render(request, 'pizzas/update_topping.html', {
                    'form': form,
                    'dup': True,
                    'id': id,
                })
            else:
                topping.name = form.cleaned_data['name'].title()
                topping.save(update_fields=['name'])
                return render(request, 'pizzas/update_topping.html', {
                    'form': form,
                    'success': True,
                    'id': id
                })
    else:
        topping = Topping.objects.get(pk=id)
        form = ToppingForm(instance=topping)
    return render(request, 'pizzas/update_topping.html', {
        'form': form,
        'id': id
    })

def delete_topping(request, id):
    if request.method == "POST":
        topping = Topping.objects.get(pk=id)
        topping.delete()
    return HttpResponseRedirect(reverse('manage_toppings'))

# All views for chef's side (manage pizzas)

def manage_pizzas(request):
    return render(request, 'pizzas/manage_pizzas.html', {
        'pizzas': Pizza.objects.all()
    })

def view_pizza(request, id):
    pizza = Pizza.objects.get(pk=id)
    return HttpResponseRedirect(reverse('manage_pizzas'))

def delete_pizza(request, id):
    if request.method == "POST":
        pizza = Pizza.objects.get(pk=id)
        pizza.delete()
    return HttpResponseRedirect(reverse('manage_pizzas'))


def add_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            toppings = form.cleaned_data['toppings']
            if is_dupplicate("p", new_name):
                return render(request, 'pizzas/add_pizza.html', {
                    'form': PizzaForm(),
                    'dup': True
                })
            new_pizza = Pizza.objects.create(name=new_name)
            
            for topping in toppings:
                new_pizza.toppings.add(topping)

            new_pizza.save()
            return render(request, 'pizzas/add_pizza.html', {
                'form': PizzaForm(),
                'success': True
            })
    else:
        form = PizzaForm()
    return render(request, 'pizzas/add_pizza.html', {
        'form': form
    })

def update_pizza(request, id):
    if request.method == "POST":
        pizza = Pizza.objects.get(pk=id)
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            if is_dupplicate(type="p", name=form.cleaned_data['name']):
                return render(request, 'pizzas/update_pizza.html', {
                    'form': form,
                    'dup': True,
                    'id': id,
                })
            else:
                pizza.name = form.cleaned_data['name'].title()
                updated_toppings = form.cleaned_data['toppings']
                pizza.toppings.clear()
                for topping in updated_toppings:
                    pizza.toppings.add(topping)
                pizza.save()
                return render(request, 'pizzas/update_pizza.html', {
                    'form': form,
                    'success': True,
                    'id': id
                })
    else:
        pizza = Pizza.objects.get(pk=id)
        form = PizzaForm(instance=pizza)
    return render(request, 'pizzas/update_pizza.html', {
        'form': form,
        'id': id
    })