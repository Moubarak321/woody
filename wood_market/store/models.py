from contextlib import nullcontext
from distutils.command.upload import upload
from email.policy import default
from tokenize import blank_re
# from unicodedata import category, name

from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(default=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0.0)
    slug = models.SlugField(max_length=200)

    category = models.ForeignKey(Category, on_delete = models.CASCADE, default= True, null= False)
    description = models.TextField(blank=False)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("detail", kwargs = {"slug": self.slug})
