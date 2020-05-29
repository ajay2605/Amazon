from django.urls import path,include
from .views import AmazonDotComView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('new_app', views.AmazonDotComView)
urlpatterns = [
    path('',include(router.urls))
]