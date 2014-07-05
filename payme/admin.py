
from django.contrib import admin

from payme.models import Account, Merchant, Product

admin.site.register(Account)
admin.site.register(Merchant)
admin.site.register(Product)
