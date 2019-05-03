from django.urls import path
from . import views

app_name='foodRecommendation'
urlpatterns = [
    path('', views.food_recommendation, name="food_recommendation"),
]