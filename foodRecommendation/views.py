from django.http import JsonResponse
from django.shortcuts import render
from foodList.models import Recipe

import random

assigned = []
solution = []

def food_recommendation(request):
    # set assigned
    assign_assigned(Recipe.objects.all().count())

    # filter domain by ingredients constraints
    domain = filter_domain(request)

    # get number of calories needed
    calory_type = request.GET.get('calories')
    total_calories = get_calories(calory_type)

    # get number of meals per day
    meals_per_day = int(request.GET.get('meals_per_day'))

    global solution
    to_return = {}
    for i in range(7):
        random.shuffle(domain)
        if search_food(domain, total_calories, meals_per_day):
            to_return[i] = solution
            solution = []
        else:
            to_return = "No solution"
            break

    return JsonResponse(to_return, safe=False)

# method to filter domain by ingredients constraints
def filter_domain(request):
    domain = Recipe.objects.all()
    assign_assigned(len(domain))
    
    alcohol = request.GET.get('contains_alcohol')
    if (alcohol == "False"):
        domain = domain.filter(alcohol=False)

    gluten = request.GET.get('contains_gluten')
    if (gluten == "False"):
        domain = domain.filter(gluten=False)

    lactose = request.GET.get('contains_lactose')
    if (lactose == "False"):
        domain = domain.filter(lactose=False)

    egg = request.GET.get('contains_egg')
    if (egg == "False"):
        domain = domain.filter(egg=False)
    
    meat = request.GET.get('contains_meat')
    if (meat == "False"):
        domain = domain.filter(meat=False)

    pork = request.GET.get('contains_pork')
    if (pork == "False"):
        domain = domain.filter(pork=False)
    
    fish = request.GET.get('contains_fish')
    if (fish == "False"):
        domain = domain.filter(fish=False)

    vegan = request.GET.get('is_vegan')
    if (vegan == "True"):
        domain = domain.filter(vegan=True)
    
    containsMilk = request.GET.get('contains_milk')
    containsMilkSubstitute = request.GET.get('contains_milk_substitute')
    if (containsMilk == "True"):
        pass
    elif (containsMilk == "False"):
        domain = domain.filter(containsMilk=False)
        if (containsMilkSubstitute == "False"):
            domain = domain.filter(containsMilkSubstitute=False)

    return list(domain.values())

# method to get number of calories by calory type
def get_calories(calory_type):
    if (calory_type == 'Diet'):
        return 1200
    if (calory_type == 'Normal'):
        return 2000
    if (calory_type == 'High Calories'):
        return 3000

def assign_assigned(n):
    for i in range(n+2):
        assigned.append(False)

def search_food(domain, total_calories, meals_per_day):
    if meals_per_day == 0:
        if abs(total_calories) < 150:
            return True
        else:
            return False

    for food in domain:
        if not assigned[food['id']]:
            assigned[food['id']] = True
            if search_food(domain, total_calories - food['recipeCalories'], meals_per_day - 1):
                to_append = dict((key, food[key]) for key in ['recipeName', 'recipeCalories'])
                solution.append(to_append)
                return True
        assigned[food['id']] = False

    return False
