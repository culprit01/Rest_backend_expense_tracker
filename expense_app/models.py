from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Expense(models.Model):
    description = models.TextField(max_length = 255)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.description