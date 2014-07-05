from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^product/$', 'get_product_price', name='get_product_price'),
    url(r'^merchant/$', 'get_merchant_phone_number', name='get_merchant_phone_number'),

    # Examples:
    url(r'^$', 'payme.views.home', name='home'),
    # url(r'^payments/', include('payments.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
