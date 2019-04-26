from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import Planner_Form
from foodList.models import Recipe

def index(request):
    response = {}
    response['planner_form'] = Planner_Form
    #debug
    print("Views complete.")
    return render(request, 'homepage/templates/index.html', response)

def submit_constraints(request):
    # create a form instance and populate it with data from the request:
    form = Planner_Form(request.POST or None)

    # check whether method is a POST and whether the form is valid
    if(request.method == 'POST' and form.is_valid()):
        print("Form accepted.")
        print(request.POST['calories'])
        print(request.POST['meals_per_day'])
        print(request.POST['contains_pork'])
        print(request.POST['contains_alcohol'])
        print(request.POST['contains_gluten'])
        print(request.POST['contains_lactose'])
        print(request.POST['contains_egg'])
        print(request.POST['contains_meat'])
        print(request.POST['is_vegan'])
        print(request.POST['contains_milk'])
        print(request.POST['contains_milk_substitute'])
        ''' response['name'] = request.POST['name']
        response['category'] = request.POST['category']
        response['location'] = request.POST['location']
        response['date'] = request.POST['date']
        response['time'] = request.POST['time']
        activity = Activity(name=response['name'], category=response['category'], location=response['location'], date=response['date'], time=response['time'])
        activity.save() '''
        return HttpResponseRedirect(reverse('homepage:index'))

    # if method is a GET (or any other method) or form is invalid, create a blank form
    else:
        print("Form not accepted.")
        return HttpResponseRedirect(reverse('homepage:index'))