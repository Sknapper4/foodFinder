from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'%s in %s' % (self.name, self.city)


class Snack(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=1.00, decimal_places=2, max_digits=6)
    date_found = models.DateTimeField(auto_now_add=True, blank=True)
    sale = models.BooleanField(default=False)
    author = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'%s' % self.name

    def pretty_price_string(self):
        fancy_price = f'$%.2f' % self.price
        return fancy_price
