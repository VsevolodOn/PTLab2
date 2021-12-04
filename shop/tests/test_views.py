from django.test import TestCase, Client
from shop.views import PurchaseCreate
from django.urls import reverse
from shop.models import Product


class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.pr = Product.objects.create(name="plant", price="740",
                                         count_now="10", count="10")

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_accessibility(self):
        response = self.client.get(reverse('buy', args=[self.pr.id]))
        self.assertEqual(response.status_code, 200)
