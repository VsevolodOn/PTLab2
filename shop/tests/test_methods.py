from django.test import TestCase
from shop.models import Product
from shop.views import update_price


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="plant", price="740",
                               count_now="3", count="10")
        Product.objects.create(name="table", price="50",
                               count_now="10", count="10")

    def test_correctness_types(self):
        update_price()
        self.assertTrue(Product.objects.get(name="plant").price == 888)
        self.assertTrue(Product.objects.get(name="table").price == 50)
