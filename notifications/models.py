from django.db import models
from workers.models import Worker, Receipt
# Create your models here.
class Notification(models.Model):
    received_receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, related_name='received_receipt')
    notification_receiver = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='notification_receiver')
    was_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"От {self.received_receipt.worker.user.username}, {self.received_receipt.date}"

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'