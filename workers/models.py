from typing import Any
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Worker(models.Model):
    user = models.OneToOneField(User, related_name="worker", unique=True, blank=True, null=True, default=None,
                                on_delete=models.CASCADE)

    first_name = models.CharField(max_length=128, blank=True, null=True, default=None) # Имя
    last_name = models.CharField(max_length=128, blank=True, null=True, default=None) # Фамилия
    surname = models.CharField(max_length=128, blank=True, null=True, default=None) # Отчество

    email = models.EmailField(blank=True, null=True, default=None)

    speciality = models.CharField(max_length=128, blank=True, null=True, default=None)
    experience = models.DecimalField(max_digits=30, decimal_places=0, blank=True, null=True, default=0)
    money = models.DecimalField(max_digits=10000, decimal_places=0, blank=True, null=True, default=0)

    city = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "Работник %s" % self.user

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


@receiver(post_save, sender=User)
def user_created(sender, instance=None, created=False, **kwargs):
    if created:
        Worker.objects.get_or_create(user=instance, )


class Receipt(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='receipts/', blank=False, null=False)

    def __str__(self):
        return "Дата добавления %s" % self.date

    class Meta:
        ordering = ['-date']
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
