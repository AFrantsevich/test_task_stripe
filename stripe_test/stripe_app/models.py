from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name',
                           'description',
                           'price')
