from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime



class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="plant", price="740",
                               count_now="10", count="10")
        Product.objects.create(name="table", price="50",
                               count_now="10", count="10")

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="plant").name, str)
        self.assertIsInstance(Product.objects.get(name="plant").price, int)
        self.assertIsInstance(Product.objects.get(name="plant").count_now, int)
        self.assertIsInstance(Product.objects.get(name="plant").count, int)
        self.assertIsInstance(Product.objects.get(name="table").name, str)
        self.assertIsInstance(Product.objects.get(name="table").price, int)
        self.assertIsInstance(Product.objects.get(
            name="table").count_now, int)
        self.assertIsInstance(Product.objects.get(name="table").count, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="plant").price == 740)
        self.assertTrue(Product.objects.get(name="table").price == 50)
        self.assertTrue(Product.objects.get(name="plant").count_now == 10)
        self.assertTrue(Product.objects.get(name="table").count_now == 10)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="plant", price="740")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.",
                                count="10")

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(
            product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(
            product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(
            product=self.product_book).date, datetime)
        self.assertIsInstance(Purchase.objects.get(
            product=self.product_book).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(
            product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(
            product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) ==
                        self.datetime.replace(microsecond=0))
