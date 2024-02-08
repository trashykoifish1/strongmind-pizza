from django.db import models

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping, blank=True)
    
    def get_toppings(self):
        return ", ".join([str(t) for t in self.toppings.all()])

    def __str__(self) -> str:
        return f"{self.name} - Toppings: {self.get_toppings()}"
