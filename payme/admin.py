
from django.contrib import admin

from payme.models import Account, Merchant, Product


class AccountAdmin(admin.ModelAdmin):
    list_display = ('mobile_number', 'current_balance')
admin.site.register(Account, AccountAdmin)


admin.site.register(Merchant)
admin.site.register(Product)
