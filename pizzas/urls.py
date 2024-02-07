from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toppings/', views.manage_toppings, name='manage_toppings'),
    path('toppings/add', views.add_topping, name='add_topping'),
    path('topping/update/<int:id>', views.update_topping, name='update_topping'),
    path('topping/delete/<int:id>', views.delete_topping, name='delete_topping'),
    path('pizzas/', views.manage_pizzas, name='manage_pizzas'),
    path('pizzas/add', views.add_pizza, name='add_pizza'),
    path('pizzas/<int:id>', views.view_pizza, name='view_pizza'),
    path('pizzas/update/<int:id>', views.update_pizza, name='update_pizza'),
    path('pizzas/delete/<int:id>', views.delete_pizza, name='delete_pizza'),
]
