from django.shortcuts import render

def index(request):
    return render(request, 'foodList/templates/index.html', {})

def breadFruitPie(request):
    return render(request, 'foodList/templates/breadFruitPie.html', {})

def basilPestoQuinoa(request):
    return render(request, 'foodList/templates/basilPestoQuinoa.html', {})

def beefCutlet(request):
    return render(request, 'foodList/templates/beefCutlet.html', {})

def carrotSticksWithDip(request):
    return render(request, 'foodList/templates/carrotSticksWithDip.html', {})

def chocolateMilkShake(request):
    return render(request, 'foodList/templates/chocolateMilkShake.html', {})

def doubleVeganPizzaWithSoyMilk(request):
    return render(request, 'foodList/templates/doubleVeganPizzaWithSoyMilk.html', {})

def lentilNutTacos(request):
    return render(request, 'foodList/templates/lentilNutTacos.html', {})

def mushroomFriedRice(request):
    return render(request, 'foodList/templates/mushroomFriedRice.html', {})

def peanutRaisinOatmeal(request):
    return render(request, 'foodList/templates/peanutRaisinOatmeal.html', {})

def penneArabiataWithSoyMilk(request):
    return render(request, 'foodList/templates/penneArabiataWithSoyMilk.html', {})

def pumpkinPie(request):
    return render(request, 'foodList/templates/pumpkinPie.html', {})

def soyMilk(request):
    return render(request, 'foodList/templates/soyMilk.html', {})

def veganLasagnaRolls(request):
    return render(request, 'foodList/templates/veganLasagnaRolls.html', {})

def veganPizzaWithSoyMilk(request):
    return render(request, 'foodList/templates/veganPizzaWithSoyMilk.html', {})