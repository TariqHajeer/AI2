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
    #if request was post 
    if(request.method == 'POST'):
        #get data from reqeust 
        fromCity = request.POST["from"]
        toCity = request.POST["to"]
        countrymap = request.POST["map"]
        datafromJson = json.loads(countrymap)
        #create object of map 
        m = map()
        for d in datafromJson:
            #if city don't equeal to it self
            if(d["from"] != d["to"]):
                #add data for map
                m.mkdir(d["from"], d["to"], int(d["value"]))
        #return the request of a star algorithm as json 
        return HttpResponse(json.dumps(astar(fromCity, toCity, m)))
    #if not post then it well be get so return home html page 
    return render(request, 'home.html')

