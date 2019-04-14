from django.shortcuts import render

def breadFruitPie(request):
    return render(request, 'foodList/templates/breadFruitPie.html', {})
