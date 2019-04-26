from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import Planner_Form
from foodList.models import Recipe

def index(request):
    response = {}
    response['planner_form'] = Planner_Form
    print("Views complete.") # debug
    return render(request, 'homepage/templates/index.html', response)

def submit_constraints(request):
    # create a form instance and populate it with data from the request:
    form = Planner_Form(request.POST or None)

    # check whether method is a POST and whether the form is valid
    if(request.method == 'POST' and form.is_valid()):
        response = {}
        print("Form accepted.") # debug
        response['calories'] = request.POST['calories']
        response['meals_per_day'] = request.POST['meals_per_day']
        response['contains_pork'] = request.POST.get('contains_pork', False) and True
        response['contains_alcohol'] = request.POST.get('contains_alcohol', False) and True
        response['contains_gluten'] = request.POST.get('contains_gluten', False) and True
        response['contains_lactose'] = request.POST.get('contains_lactose', False) and True
        response['contains_egg'] = request.POST.get('contains_egg', False) and True
        response['contains_meat'] = request.POST.get('contains_meat', False) and True
        response['is_vegan'] = request.POST.get('is_vegan', False) and True
        response['contains_milk'] = request.POST.get('contains_milk', False) and True
        response['contains_milk_substitute'] = request.POST.get('contains_milk_substitute', False) and True
        print(response) # debug
        return HttpResponseRedirect(reverse('homepage:index'))

    # if method is a GET (or any other method) or form is invalid, create a blank form
    else:
        print("Form not accepted.") # debug
        return HttpResponseRedirect(reverse('homepage:index'))