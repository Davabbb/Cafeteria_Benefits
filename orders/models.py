from django.db import models
from products.models import Product


class Order(models.Model):
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "Заказ %s" % self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Льгота'
        verbose_name_plural = 'Льготы'
