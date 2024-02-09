from django.test import TestCase
from django.urls import reverse
from .models import Pizza, Topping

# Create your tests here.

# Model tests
class ToppingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Topping.objects.create(name='Pepperoni')
    
    def test_topping_name_label(self):
        topping = Topping.objects.get(id=1)
        field_label = topping._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        topping = Topping.objects.get(id=1)
        max_length = topping._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_object_returned_name_string(self):
        topping = Topping.objects.get(id=1)
        expected_object_name = topping.name
        self.assertEqual(str(topping), expected_object_name)

class PizzaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        toppings = [Topping.objects.create(name='Pepperoni'), Topping.objects.create(name='Cheese'), Topping.objects.create(name='Olives')]
        pizza = Pizza.objects.create(name='Pizza #1')
        for topping in toppings:
            pizza.toppings.add(topping)
    
    def test_pizza_name_label(self):
        pizza = Pizza.objects.get(id=1)
        field_label = pizza._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_pizza_toppings_label(self):
        pizza = Pizza.objects.get(id=1)
        field_label = pizza._meta.get_field('toppings').verbose_name
        self.assertEqual(field_label, 'toppings')
    
    def test_pizza_object_returned_string(self):
        pizza = Pizza.objects.get(id=1)
        expected_object_name = f"{pizza.name} - Toppings: Pepperoni, Cheese, Olives"
        self.assertEqual(str(pizza), expected_object_name)

# View tests
class AccessToppingViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        number_of_toppings = 10
        for i in range(number_of_toppings):
            Topping.objects.create(name=f"Topping {i}")
    
    def test_all_toppings_view_exist(self):
        response = self.client.get('/toppings/')
        self.assertEqual(response.status_code, 200)
    
    def test_all_toppings_view_accessible_by_name(self):
        response = self.client.get(reverse('manage_toppings'))
        self.assertEqual(response.status_code, 200)


    def test_all_toppings_view_correct_template(self):
        response = self.client.get(reverse('manage_toppings'))
        self.assertTemplateUsed(response, 'pizzas/toppings.html')

    def test_add_topping_view_correct_template(self):
        response = self.client.get(reverse('add_topping'))
        self.assertTemplateUsed(response, 'pizzas/add_topping.html')

    def test_accessing_update_page_for_all_toppings(self):
        for i in range(10):
            response = self.client.get(f'/toppings/update/{i}')
            self.assertTrue(response.status_code, 200)
    
    def test_accessing_delete_page_for_all_toppings(self):
        for i in range(10):
            response = self.client.get(f'/toppings/delete/{i}')
            self.assertTrue(response.status_code, 200)

class AccessPizzaViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        number_of_pizzas = 5
        test_topping = Topping.objects.create(name="Test Topping")
        for i in range(number_of_pizzas):
            pizza = Pizza.objects.create(name=f"Pizza #{i}")
            pizza.toppings.add(test_topping)
        
    def test_all_pizzas_view_exist(self):
        response = self.client.get('/pizzas/')
        self.assertEqual(response.status_code, 200)
    
    def test_all_pizzas_view_accessible_by_name(self):
        response = self.client.get(reverse('manage_pizzas'))
        self.assertEqual(response.status_code, 200)


    def test_all_pizzas_view_correct_template(self):
        response = self.client.get(reverse('manage_pizzas'))
        self.assertTemplateUsed(response, 'pizzas/manage_pizzas.html')

    def test_add_pizza_view_correct_template(self):
        response = self.client.get(reverse('add_pizza'))
        self.assertTemplateUsed(response, 'pizzas/add_pizza.html')

    # Using i+1 to account for the 1 topping created
    def test_accessing_view_page_for_all_pizzas(self):
        for i in range(5):
            response = self.client.get(f'/pizzas/{i+1}')
            self.assertTrue(response.status_code, 200)

    def test_accessing_update_page_for_all_pizzas(self):
        for i in range(5):
            response = self.client.get(f'/pizzas/update/{i+1}')
            self.assertTrue(response.status_code, 200)
    
    def test_accessing_delete_page_for_all_pizzas(self):
        for i in range(5):
            response = self.client.get(f'/pizzas/delete/{i+1}')
            self.assertTrue(response.status_code, 200)
        