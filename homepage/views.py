from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import Planner_Form
from foodList.models import Recipe
from foodRecommendation.views import food_recommendation

import requests
import json

form_response = {}

def index(request):
    global form_response
    response = {}
    response['planner_form'] = Planner_Form
    response['has_submit_constraints_form'] = bool(form_response)
    if (bool(form_response)):
        response.update(form_response)
        form_response = {}
        response['all_recipes'] = Recipe.objects.all().values()
    print("Views complete.") # debug
    return render(request, 'homepage/templates/index.html', response)

def submit_constraints(request):
    global form_response
    
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
        # print(form_response) # debug
        something = food_recommendation(form_response)
        print(something)
        return JsonResponse(something, safe=False)

    # if method is a GET (or any other method) or form is invalid, create a blank form
    else:
        print("Form not accepted.") # debug
        return HttpResponseRedirect(reverse('homepage:index'))