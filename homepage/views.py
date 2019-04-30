from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import Planner_Form
from foodList.models import Recipe

import requests
import json

form_response = {}

def index(request):
    global form_response
    response = {}
    response['planner_form'] = Planner_Form
    response['has_submit_constraints_form'] = bool(form_response)
    response.update(form_response)
    form_response = {}
    print("Views complete.") # debug
    return render(request, 'homepage/templates/index.html', response)

def submit_constraints(request):
    global form_response
    
    # create a form instance and populate it with data from the request:
    form = Planner_Form(request.POST or None)

    # check whether method is a POST and whether the form is valid
    if(request.method == 'POST' and form.is_valid()):
        print("Form accepted.") # debug
        form_response['calories'] = request.POST['calories']
        form_response['meals_per_day'] = request.POST['meals_per_day']
        form_response['contains_alcohol'] = request.POST.get('contains_alcohol', False) and True
        form_response['contains_gluten'] = request.POST.get('contains_gluten', False) and True
        form_response['contains_lactose'] = request.POST.get('contains_lactose', False) and True
        form_response['contains_egg'] = request.POST.get('contains_egg', False) and True
        form_response['contains_meat'] = request.POST.get('contains_meat', False) and True
        form_response['contains_pork'] = request.POST.get('contains_pork', False) and True
        form_response['contains_fish'] = request.POST.get('contains_fish', False) and True
        form_response['is_vegan'] = request.POST.get('is_vegan', False) and True
        form_response['contains_milk'] = request.POST.get('contains_milk', False) and True
        form_response['contains_milk_substitute'] = request.POST.get('contains_milk_substitute', False) and True
        # print(form_response) # debug
        something = requests.get('http://localhost:8000/foodRecommendation/', form_response)
        aaa = json.loads(something.text)
        return JsonResponse(aaa, safe=False)
        return HttpResponseRedirect(reverse('homepage:index'))

    # if method is a GET (or any other method) or form is invalid, create a blank form
    else:
        print("Form not accepted.") # debug
        return HttpResponseRedirect(reverse('homepage:index'))