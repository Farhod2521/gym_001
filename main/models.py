from re import M
from django.urls import reverse
from django.db import models


class HodAdmin(models.Model):
    full_name  = models.CharField(max_length=200, verbose_name="Ism Familya")
    phone = models.CharField(max_length=200, verbose_name="Telfon raqam")
    username  = models.CharField(max_length=200, verbose_name="Username")
    password =  models.CharField(max_length=200, verbose_name="Parol")


    def register(self):
        self.save()

    def __str__(self) -> str:
        return self.full_name


    @staticmethod
    def get_customer_by_username(username):
        try:
            return HodAdmin.objects.get(username = username)
        except:
            return False

class Customers(models.Model):
    full_name  =  models.CharField(max_length=200, verbose_name="Ism Familya")
    phone = models.CharField(max_length=200, verbose_name="Telfon raqam")
    image = models.ImageField(upload_to = "Rasm", verbose_name="Rasm", null=True, blank=True)
    data = models.DateTimeField(auto_now=False)


    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('customers_table')






# Create your models here.
