from django.db import models


class AmazonDotCom(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

