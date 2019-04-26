from django.shortcuts import render
from foodList.models import Recipe

def foodRecomendation(request):
    return render(request,'homepage/templates/index.html', {})

def filterDomain(request):
    pork = False
    alcohol = False
    gluten = False
    lactose = False
    egg = False
    meat = False
    vegan = False
    containsMilk = False
    containsMilkSubstitute = False

    domain = Recipe.objects.all()
    domain = domain.filter(pork=pork, alcohol=alcohol, gluten=gluten, lactose=lactose, egg=egg,
                vegan=vegan, meat=meat, containsMilk=containsMilk, containsMilkSubstitute=containsMilkSubstitute)
    print(domain)
    return render(request,'homepage/templates/index.html', {})