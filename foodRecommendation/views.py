from django.http import JsonResponse
from django.shortcuts import render
from foodList.models import Recipe

import json

def foodRecomendation(request):
    domain = filterDomain(request)
    print(domain)
    return JsonResponse(domain, safe=False)

def filterDomain(request):
    alcohol = request.GET.get('contains_alcohol')
    gluten = request.GET.get('contains_gluten')
    lactose = request.GET.get('contains_lactose')
    egg = request.GET.get('contains_egg')
    meat = request.GET.get('contains_meat')
    pork = request.GET.get('contains_pork')
    fish = request.GET.get('contains_fish')
    vegan = request.GET.get('is_vegan')
    containsMilk = request.GET.get('contains_milk')
    containsMilkSubstitute = request.GET.get('contains_milk_substitute')

    domain = Recipe.objects.filter(pork=pork, alcohol=alcohol, gluten=gluten, lactose=lactose, egg=egg, #fish=fish,
                vegan=vegan, meat=meat, containsMilk=containsMilk, containsMilkSubstitute=containsMilkSubstitute).values()
    return list(domain)