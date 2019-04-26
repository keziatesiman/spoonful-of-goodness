from django.urls import path
from . import views

app_name='foodRecommendation'
urlpatterns = [
    path('', views.foodRecomendation, name="foodRecommendation"),
]