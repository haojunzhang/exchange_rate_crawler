from django.db import models


class ExchangeRate(models.Model):
    source = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    rate_buy = models.CharField(max_length=20)
    rate_sell = models.CharField(max_length=20)
    create_time = models.DateTimeField()

    def __str__(self):
        return f'{self.create_time} {self.source} {self.currency} {self.rate}'
