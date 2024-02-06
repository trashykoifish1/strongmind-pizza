from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toppings/', views.manage_toppings, name='manage_toppings'),
    path('toppings/add', views.add_topping, name='add_topping'),
]
