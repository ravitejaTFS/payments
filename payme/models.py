
from django.db import models


class Account(models.Model):
    mobile_number = models.CharField(max_length=10)
    is_active = models.BooleanField()
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='debits')
    to_account = models.ForeignKey(Account, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Merchant(models.Model):
    merchant_id = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True, max_length=10)
    account = models.ForeignKey(Account)
    description = models.TextField()


class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()