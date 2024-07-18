from django.db import models
from django.utils import timezone
from datetime import date

class Currency(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'AQSH dollari'),
        ('EUR', 'Yevro'),
        ('GBP', 'Britaniya Funt sterlingi'),
        ('RUB', 'Rus rubli'),
        ('KZT', 'Qozoq Tenge'),
    ]

    code = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    sell_rate = models.DecimalField(max_digits=20, decimal_places=2)
    buy_rate = models.DecimalField(max_digits=20, decimal_places=2)
    upload_time = models.DateField(default=date.today)

    class Meta:
        unique_together = ('code', 'upload_time')

    def save(self, *args, **kwargs):
        self.upload_time = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_code_display()} - {self.rate_to_uzs}"

    