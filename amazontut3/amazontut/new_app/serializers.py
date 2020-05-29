from rest_framework import serializers
from .models import AmazonDotCom


class AmazonDotComSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmazonDotCom
        fields = ('id','url','title','price')
        # the above line is like a form, it gives forms for us to create data. We can customise these using the fields
        # variable.

