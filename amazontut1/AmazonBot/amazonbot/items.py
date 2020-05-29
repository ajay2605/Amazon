
from scrapy_djangoitem import DjangoItem
from new_app.models import AmazonDotCom


class AmazonDotComItem(DjangoItem):
    django_model = AmazonDotCom

