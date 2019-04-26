from django.shortcuts import render

def index(request):
    return render(request, 'foodList/templates/index.html', {})

def breadFruitPie(request):
    return render(request, 'foodList/templates/breadFruitPie.html', {})
