from django.urls import path
from . import views

app_name='foodList'
urlpatterns = [
    path('', views.index, name="index"),
    path('breadFruitPie/', views.breadFruitPie, name="breadFruitPie"),
    path('beefCutlet/', views.beefCutlet, name="beefCutlet"),
    path('basilPestoQuinoa/', views.basilPestoQuinoa, name="basilPestoQuinoa"),
    path('carrotSticksWithDip/', views.carrotSticksWithDip, name="carrotSticksWithDip"),
    path('chocolateMilkShake/', views.chocolateMilkShake, name="chocolateMilkShake"),
    path('doubleVeganPizzaWithSoyMilk/', views.doubleVeganPizzaWithSoyMilk, name="doubleVeganPizzaWithSoyMilk"),
    path('lentilNutTacos/', views.lentilNutTacos, name="lentilNutTacos"),
    path('mushroomFriedRice/', views.mushroomFriedRice, name="mushroomFriedRice"),
    path('peanutRaisinOatmeal/', views.peanutRaisinOatmeal, name="peanutRaisinOatmeal"),
    path('penneArabiataWithSoyMilk/', views.penneArabiataWithSoyMilk, name="penneArabiataWithSoyMilk"),
    path('pumpkinPie/', views.pumpkinPie, name="pumpkinPie"),
    path('soyMilk/', views.soyMilk, name="soyMilk"),
    path('veganLasagnaRolls/', views.veganLasagnaRolls, name="veganLasagnaRolls"),
    path('veganPizzaWithSoyMilk/', views.veganPizzaWithSoyMilk, name="veganPizzaWithSoyMilk"),
    path('vegetableMeat/', views.vegetableMeat, name="vegetableMeat"),
    path('porkChopWithMashedPotatoes/', views.porkChopWithMashedPotatoes, name="porkChopWithMashedPotatoes"),
    path('cerealWithFruit/', views.cerealWithFruit, name="cerealWithFruit"),
    path('tunaCucumberWrap/', views.tunaCucumberWrap, name="tunaCucumberWrap"),
    path('scrambledEggs/', views.scrambledEggs, name="scrambledEggs"),
    path('bananaBread/', views.bananaBread, name="bananaBread"),
    path('caesarSalad/', views.caesarSalad, name="caesarSalad"),
    path('californiaRollSushi/', views.californiaRollSushi, name="californiaRollSushi"),
    path('greenSaladWithHoneyLemonChicken/', views.greenSaladWithHoneyLemonChicken, name="greenSaladWithHoneyLemonChicken"),
]