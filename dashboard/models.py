from django.db import models

# Create your models here.

class BCHData(models.Model):
    current_price = models.IntegerField()

    def saveData(self):
        self.save()