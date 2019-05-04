from django.http import JsonResponse
from django.shortcuts import render
from foodList.models import Recipe

import random

assigned = []
solution = []

def food_recommendation(form_response):
    # filter domain by ingredients constraints
    domain = filter_domain(form_response)
    
    # get number of calories needed
    calory_type = form_response['calories']
    total_calories = get_calories(calory_type)

    # get number of meals per day
    meals_per_day = int(form_response['meals_per_day'])

    global solution
    to_return = {}
    all_domain_size = Recipe.objects.all().count()
    for i in range(7):
        random.shuffle(domain)
        set_assigned_to_false(all_domain_size)
        if search_food(domain, total_calories, meals_per_day):
            to_return[i] = solution
            solution = []
        else:
            to_return = "No solution"
            break

    return to_return

# method to filter domain by ingredients constraints
def filter_domain(form_response):
    domain = Recipe.objects.all()
    
    alcohol = form_response['contains_alcohol']
    if not alcohol:
        domain = domain.filter(alcohol=False)

    gluten = form_response['contains_gluten']
    if not gluten:
        domain = domain.filter(gluten=False)

    lactose = form_response['contains_lactose']
    if not lactose:
        domain = domain.filter(lactose=False)

    vegan = form_response['is_vegan']
    if vegan:
        domain = domain.filter(vegan=True)

    egg = form_response['contains_egg']
    if not egg:
        domain = domain.filter(egg=False)
    
    meat = form_response['contains_meat']
    if not meat:
        domain = domain.filter(meat=False)

    pork = form_response['contains_pork']
    if not pork:
        domain = domain.filter(pork=False)
    
    fish = form_response['contains_fish']
    if not fish:
        domain = domain.filter(fish=False)
    
    containsMilk = form_response['contains_milk']
    containsMilkSubstitute = form_response['contains_milk_substitute']
    if containsMilk:
        pass
    else:
        domain = domain.filter(containsMilk=False)
        if not containsMilkSubstitute:
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

def set_assigned_to_false(n):
    global assigned
    assigned = []
    for i in range(n+2):
        assigned.append(False)

def search_food(domain, total_calories, meals_per_day):
    if meals_per_day == 0:
        if abs(total_calories) < 150:
            return True
        else:
            return False

    for food in domain:
        global assigned
        if not assigned[food['id']]:
            assigned[food['id']] = True
            if search_food(domain, total_calories - food['recipeCalories'], meals_per_day - 1):
                to_append = dict((key, food[key]) for key in ['recipeName', 'recipeCalories'])
                solution.append(to_append)
                return True
            assigned[food['id']] = False

    return False
