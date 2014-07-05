import os
import sys
from site import addsitedir
from os.path import abspath, dirname, join

path='/var/www/payments'

sys.path.append('/var/www/payments/static')
sys.path.append('/var/www/payments')
sys.path.append('/var/www') # this line solved it

#sys.executable = '/home/virtualenvs/rtfs/bin/python'

#path = addsitedir(abspath(join(dirname(__file__), '../taxisforsure')), set())

if path: sys.path = list(path) + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'payments.settings'

#activate_this = '/home/virtualenvs/rtfs/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
