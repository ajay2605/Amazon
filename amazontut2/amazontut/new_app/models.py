from django.db import models

# Create your models here.

class AmazonDotCom(models.Model):
    title = models.CharField(max_length=34)
    price = models.CharField(max_length=34)

    def __str__(self):
        return self.title, self.price