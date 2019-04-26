from django.urls import path
from . import views

app_name='foodList'
urlpatterns = [
    path('', views.index, name="index"),
    path('breadFruitPie/', views.breadFruitPie, name="breadFruitPie"),
]