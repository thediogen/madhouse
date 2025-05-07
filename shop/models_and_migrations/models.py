from django.db import models

# Create your models here.

# INT VS UUID

def example_func():
    return ["1", "faf", "ad"]

class Child(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(default=18, unique=True)
    email = models.EmailField(default=255, unique=True)
    fav_toy = models.CharField(max_length=255, blank=False, default="")

# class Product(models.Model):
#     id = models.UUIDField()
#
#     title = models.CharField()
#     description = models.TextField()
#     email = models.EmailField(max_length=254)
#     url_image = models.URLField(max_length=200)
#     is_discount = models.BooleanField(default=True)
#     aaa = models.NullBooleanField()
#
#     count = models.IntegerField()
#     count2 = models.PositiveSmallIntegerField
#     count3 = models.BigAutoField()
#
#     price = models.FloatField()
#     price2 = models.DecimalField()
#
#     create = models.TimeField()
#     expiration_time = models.DurationField()
#
#     image = models.BinaryField()
#     ippp = models.GenericIPAddressField() # IPv4 або IPv6
#
#     KINDS = (('B', 'Buy'),('S', 'Sell'),('C', 'Change'))
#     kind = models.CharField(max_length=1, choices=KIND)



class GoITeeens (models.Model) :
    class Kinds(models.TextChoices):
        BUY = 'b', 'Buy'
        SELL = 's', 'Sell'
        EXCHANGE = 'с', 'Change'
        RENT = 'r'
    kind = models.CharField(max_length=1, choices=Kinds.choices, blank=True)