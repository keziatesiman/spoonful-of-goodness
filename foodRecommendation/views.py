from django.http import JsonResponse
from django.shortcuts import render
from foodList.models import Recipe

import json

def food_recommendation(request):
    # filter domain by ingredients constraints
    domain = filter_domain(request)

    # get number of calories needed
    calory_type = request.GET.get('calories')
    total_calories = get_calories(calory_type)

    # get number of meals per day
    meals_per_day = request.GET.get('meals_per_day')

    return JsonResponse(domain, safe=False)

# method to filter domain by ingredients constraints
def filter_domain(request):
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

# method to get number of calories by calory type
def get_calories(calory_type):
    if (calory_type == 'Diet'):
        return 1000
    if (calory_type == 'Normal'):
        return 2000
    if (calory_type == 'High Calories'):
        return 3000

def search_food():
    pass