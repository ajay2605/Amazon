from django.db import models

class AmazonDotCom(models.Model):
    title = models.CharField(max_length=240)
    price = models.CharField(max_length= 20)

    def __str__(self):
        return self.title ,self.price
