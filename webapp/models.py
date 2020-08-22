from django.db import models


# Create your models here.
class Cricketers(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=15)
    player_id = models.IntegerField()

    def __str__(self):
        return self.name
