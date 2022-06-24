from cmath import log
import imp
import json
from os import mkdir
import this
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from demo.Astar import makedict,astar,romania


# Create your views here.
def home(request):
    if(request.method=='POST'):
        fromCity= request.POST["from"]
        toCity = request.POST["to"]
        countrymap = request.POST["map"]
        datafromJson= json.loads(countrymap)
        
        
        for d in datafromJson:
            makedict(d["from"],d["to"],int( d["value"]))

        return HttpResponse(json.dumps(romania))
    
    return render(request,'home.html',{"name":'taaa'})

