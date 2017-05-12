from django.shortcuts import render
from django.http import HttpResponse
from league.models import MettEater, Metting

def index(request):
    return HttpResponse("Hello Mett eater.")

def table(request):
    mett_table = []
    for eater in MettEater.objects.all():
        organized_mettings = eater.organized_mettings
        provided_meals = 0
        taken_meals = 0
        for metting in organized_mettings.all():
            provided_meals += len(metting.eaters.all()) + 1
            taken_meals += 1
        taken_meals += len(eater.metting_set.all())
        mett_table.append({'name': str(eater), 'provided_meals': provided_meals, 'taken_meals': taken_meals, 'diff': provided_meals - taken_meals})
    return render(request, 'league/table.html', context={'mett_table': sorted(mett_table, key=lambda eater: eater['diff'], reverse=True)})
