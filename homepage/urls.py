from django.urls import path
from . import views

app_name='homepage'
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.index, name="home"),
    path('submit-constraints/', views.submit_constraints, name="submit-constraints"),
]