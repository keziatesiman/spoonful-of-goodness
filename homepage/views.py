from django.shortcuts import render
from .forms import Planner_Form

def index(request):
    response = {}
    response['planner_form'] = Planner_Form
    return render(request, 'homepage/templates/index.html', response)
