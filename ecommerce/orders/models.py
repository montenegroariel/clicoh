import requests
from requests.exceptions import ConnectionError

from django.db import models
from django.db.models import Sum, F
from products.models import Product


class Order(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date_time)

    def get_total(self) -> float:
        """get the total of the products"""
        total = OrderDetail.objects.filter(order=self.pk).aggregate(total=Sum(F('product__price')*F('cuantity')))
        return total['total']

    def get_total_usd(self) -> float:
        """get the value of the price in updated dollars"""
        try:
            url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
            resp = requests.get(url, timeout=2.5).json()
            dolar = float(str(resp[1]['casa']['compra']).replace(",", "."))
            total = OrderDetail.objects.filter(order=self.pk).aggregate(total=Sum(F('product__price')*F('cuantity'))/dolar)
            return round(total['total'], 2)
        except ConnectionError as error:
            return "ERROR: " + str(error)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    cuantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '%d: %s' % (self.cuantity, self.product)
