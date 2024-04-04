from django.db import models


class Menu(models.Model):
    titles = models.CharField(max_length=10)

    def __str__(self):
        return self.titles

class Pizza(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    class_name = models.CharField(max_length=100, default='pizza')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(max_length=200)

    def __str__(self):
        return self.title

class Sushi(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    class_name = models.CharField(max_length=100, default='sushi')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(max_length=200)

    def __str__(self):
        return self.title

class Set(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    class_name = models.CharField(max_length=100, default='sets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(max_length=200)

    def __str__(self):
        return self.title

