# Generated by Django 5.0.1 on 2024-02-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_alter_pizza_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
