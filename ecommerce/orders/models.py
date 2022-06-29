import requests
from requests.exceptions import ConnectionError

from django.db import models
from products.models import Product


class Order(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date_time)

    def get_total(self) -> float:
        """get the total of the products

        Returns:
            [float]: [the result of multiplying the price by the quantity]
        """
        order_details = OrderDetail.objects.filter(order=self.pk)
        total = 0.0
        for detail in order_details:
            total += detail.product.price * detail.cuantity
        return total

    def get_total_usd(self) -> Optional[float]:
        """get the value of the price in updated dollars

        Returns:
            [float]: [result of dividing the total price by the value of the dollar]
        """
        try:
            url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
            resp = requests.get(url, timeout=1.5).json()
            dolar = resp[0]['casa']['venta']
            order_details = OrderDetail.objects.filter(order=self.pk)
            total = 0.0
            for detail in order_details:
                total = detail.product.price / float(str(dolar).replace(",", ".")) 
            return round(total, 2)
        except ConnectionError as error:
            return "ERROR: " + str(error)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    cuantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return '%d: %s' % (self.cuantity, self.product)
