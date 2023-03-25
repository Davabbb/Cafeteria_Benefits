from django.db import models
from products.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save

'''
class Order(models.Model):
    user = models.ForeignKey(User, related_name="cart", unique=True, blank=True, null=True, default=None, on_delete=models.CASCADE)
    benefit = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    date_purchased = models.DateTimeField(auto_now_add=True)                                

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

'''