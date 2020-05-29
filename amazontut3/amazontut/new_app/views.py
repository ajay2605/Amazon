from django.shortcuts import render
from rest_framework import viewsets

from .models import AmazonDotCom
from .serializers import AmazonDotComSerializer

class AmazonDotComView(viewsets.ModelViewSet):

    queryset = AmazonDotCom.objects.all()
    serializer_class = AmazonDotComSerializer

