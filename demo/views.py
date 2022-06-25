from cmath import log
import imp
import json
from os import mkdir
import this
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from demo.Astar import map, astar
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def home(request):
    return render(request, 'home.html')

def path(request):
    if(request.method == 'POST'):
        fromCity = request.POST["from"]
        toCity = request.POST["to"]
        countrymap = request.POST["map"]
        datafromJson = json.loads(countrymap)
        m = map()
        for d in datafromJson:
            if(d["from"] != d["to"]):
                m.mkdir(d["from"], d["to"], int(d["value"]))

        return HttpResponse(json.dumps(astar(fromCity, toCity, m)))
    else:
        return Http404()
