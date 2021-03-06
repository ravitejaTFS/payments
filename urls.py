from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'payme.views.home', name='home'),
    url(r'^make_payment/$', 'payme.views.make_payment', name='make_payment'),
    url(r'^recharge_account/$', 'payme.views.recharge_account', name='recharge_account'),
    url(r'^product/$', 'payme.views.get_product_price', name='get_product_price'),
    url(r'^merchant/$', 'payme.views.get_merchant_number', name='get_merchant_phone_number'),

    # url(r'^payments/', include('payments.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
