from django.test import TestCase

# Create your tests here.

import datetime
expires=datetime.datetime.now()+datetime.timedelta(days=2)
print(expires)