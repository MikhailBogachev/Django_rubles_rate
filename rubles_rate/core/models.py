from django.db import models


class RublesRate(models.Model):
    charcode = models.CharField(max_length=3)
    date = models.DateField()
    rate = models.FloatField()

    def __str__(self):
        return f'{self.charcode}_{str(self.date)}'

    class Meta:
        unique_together = ('charcode', 'date')
