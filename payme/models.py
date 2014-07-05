
from django.db import models


class Account(models.Model):
    mobile_number = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='debits')
    to_account = models.ForeignKey(Account, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
