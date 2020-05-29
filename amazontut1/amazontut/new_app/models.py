from django.db import models

class AmazonDotCom(models.Model):
    title = models.CharField(max_length=23)
    price = models.CharField(max_length=23)

    def __str__(self):
        return self.title, self.price

