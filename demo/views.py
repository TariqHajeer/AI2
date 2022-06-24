from cmath import log
import imp
import json
from os import mkdir
import this
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from demo.Astar import map,astar


# Create your views here.
def home(request):
    if(request.method=='POST'):
        fromCity= request.POST["from"]
        toCity = request.POST["to"]
        countrymap = request.POST["map"]
        datafromJson= json.loads(countrymap)
        
        m = map()
        for d in datafromJson:
            m.mkdir(d["from"],d["to"],int( d["value"]))

        return HttpResponse(json.dumps( astar(fromCity,toCity,m)))
    
    return render(request,'home.html',{"name":'taaa'})

