from django.db import models

# Create your models here.

class BCHData(models.Model):
    price = models.FloatField()
    date_of_price = models.DateField(auto_now_add=True)

    @classmethod
    def create(cls, new_price):
        bch = cls(price=new_price)
        bch.saveData()

    def saveData(self):
        self.save()