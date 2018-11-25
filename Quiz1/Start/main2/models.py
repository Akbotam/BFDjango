from django.db import models
from django.contrib.auth.models import User


class Advert(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    number_of_views = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title