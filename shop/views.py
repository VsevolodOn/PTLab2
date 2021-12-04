from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.db.models import Count, F, Value
from django.urls import reverse
from .models import Product, Purchase


def index(request):
    update_price()
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def update_price():
    prod_less = Product.objects.filter(count_now__lt=F('count')/2)
    if len(prod_less) != 0:
        for prod in prod_less:
            prod.price = prod.price*1.2
            prod.count = prod.count_now
            prod.save()


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['count', 'product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        count_buy = self.object.count
        product_buy = self.object.product
        product_buy.count_now = product_buy.count_now - count_buy
        product_buy.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!, <a href="/">Купить</a>')
