import unittest
from django.test import Client
from order.views import getcode
from django.core.urlresolvers import resolve

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_getCode(self):
        # Issue a GET request.
        phone ='13910674516'
        YZM = getcode()
        print('YZM = '+YZM)
        #found = resolve('send_code')
        #print(found)
        response = self.client.post('/api/user/send_code/',{'phone': phone, 'YZM': YZM}   )
        print (response.content )

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(response.json()['res'], 1)