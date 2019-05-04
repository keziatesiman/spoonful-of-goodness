from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import Planner_Form
from foodList.models import Recipe
from foodRecommendation.views import food_recommendation

import requests
import json

form_response = {}
json_response = {}

def index(request):
    global form_response
    global json_response
    response = {}
    response['planner_form'] = Planner_Form
    response['has_submit_constraints_form'] = bool(form_response)
    if (bool(form_response)):
        # should do something with json_response first
        dict_of_recipes = get_recipes_from_json(json_response)
        form_response = {}
        json_response = {}
        response["planned_recipes"] = dict_of_recipes
        print(response["planned_recipes"]) # debug
    print("Views complete.") # debug
    return render(request, 'homepage/templates/index.html', response)

def home(request):
    return HttpResponseRedirect(reverse('homepage:index'))

def submit_constraints(request):
    global form_response
    global json_response
    
    # create a form instance and populate it with data from the request:
    form = Planner_Form(request.POST or None)

    # check whether method is a POST and whether the form is valid
    if(request.method == 'POST' and form.is_valid()):
        print("Form accepted.") # debug
        form_response['calories'] = form.cleaned_data['calories']
        form_response['meals_per_day'] = form.cleaned_data['meals_per_day']
        form_response['contains_alcohol'] = form.cleaned_data['contains_alcohol']
        form_response['contains_gluten'] = form.cleaned_data['contains_gluten']
        form_response['contains_lactose'] = form.cleaned_data['contains_lactose']
        form_response['contains_egg'] = form.cleaned_data['contains_egg']
        form_response['contains_meat'] = form.cleaned_data['contains_meat']
        form_response['contains_pork'] = form.cleaned_data['contains_pork']
        form_response['contains_fish'] = form.cleaned_data['contains_fish'] 
        form_response['is_vegan'] = form.cleaned_data['is_vegan']
        form_response['contains_milk'] = form.cleaned_data['contains_milk']
        form_response['contains_milk_substitute'] = form.cleaned_data['contains_milk_substitute']
        print(form_response) # debug
        
        json_response = get_json_of_food_recommendation(form_response)
        print(json_response) #debug
        return HttpResponseRedirect(reverse('homepage:index'))

    # if method is a GET (or any other method) or form is invalid, create a blank form
    else:
        print("Form not accepted.") # debug
        return HttpResponseRedirect(reverse('homepage:index'))

def get_json_of_food_recommendation(form_response):
    something = food_recommendation(form_response)
    print(something) #debug
    return JsonResponse(something, safe=False)

def get_recipes_from_json(json_response):
    '''
    Example of the json_response
    {
        "0": [{"recipeName": "lentilNutTacos", "recipeCalories": 740}, {"recipeName": "veganLasagnaRolls", "recipeCalories": 344}], 
        "1": [{"recipeName": "porkChopWithMashedPotatoes", "recipeCalories": 900}, {"recipeName": "carrotSticksWithDip", "recipeCalories": 350}], 
        "2": [{"recipeName": "lentilNutTacos", "recipeCalories": 740}, {"recipeName": "greenSaladWithHoneyLemonChicken", "recipeCalories": 380}], 
        "3": [{"recipeName": "porkChopWithMashedPotatoes", "recipeCalories": 900}, {"recipeName": "honeyLemonChicken", "recipeCalories": 320}], 
        "4": [{"recipeName": "porkChopWithMashedPotatoes", "recipeCalories": 900}, {"recipeName": "beefCutlet", "recipeCalories": 300}], 
        "5": [{"recipeName": "porkChopWithMashedPotatoes", "recipeCalories": 900}, {"recipeName": "caesarSalad", "recipeCalories": 230}], 
        "6": [{"recipeName": "porkChopWithMashedPotatoes", "recipeCalories": 900}, {"recipeName": "peanutRaisinOatmeal", "recipeCalories": 204}]
    }
    '''
    recipe_dict = {} # dict with days as key and list of model objects as value

    dict_of_days = {
        "0": "Sunday",
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
    }
    print(type(json_response.content)) #debug
    print(json_response.content) #debug
    dict_from_json = json.loads(json_response.content.decode("utf-8"))

    for key in dict_from_json.keys():
        day = dict_of_days[key]
        day_food_list = dict_from_json[key] # list of dictionaries

        list_of_recipe_for_day = change_list_of_dictionaries_to_list_of_model_objects(day_food_list) # list of model objects
        
        recipe_dict[day] = list_of_recipe_for_day
    
    return recipe_dict

def change_list_of_dictionaries_to_list_of_model_objects(day_food_list):
    list_of_recipe_for_day = [] # list of model objects
    for dictio in day_food_list:
        recipe_object = (Recipe.objects.filter(recipeName = dictio["recipeName"]))[0].recipeName
        list_of_recipe_for_day.append(recipe_object)
    return list_of_recipe_for_day