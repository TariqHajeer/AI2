from cmath import log
import imp
import json
from os import mkdir
import this
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import heapq


    

class priorityQueue:
    def __init__(self):
        self.cities = []

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False

    def check(self):
        print(self.cities)


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


romania = {}


def makedict(city1,city2,distance1):
    if distance1 > 0:
        romania.setdefault(city1, []).append(ctNode(city2, distance1))





def heuristic(node, values):
    return values[node]


def astar(start, end):
    path = {}
    distance = {}
    q = priorityQueue()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandedList = []

    while (q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if (current == end):
            break

        for new in romania[current]:
            g_cost = distance[current] + int(new.distance)

            # print(new.city, new.distance, "now : " + str(distance[current]), g_cost)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost
                q.push(new.city, f_cost)
                path[new.city] = current
    return output(start, end, path, distance, expandedList)


def output(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    return {'exploredCities':str(expandedlist),"possibleCities":str(len(expandedlist)),"skippedCities":str(len(finalpath)),"path":str(finalpath),"totalDistance":str(distance[end])}


# Create your views here.
def home(request):
    if(request.method=='POST'):
        fromCity= request.POST["from"]
        toCity = request.POST["to"]
        countrymap = request.POST["map"]
        datafromJson= json.loads(countrymap)
        
        
        for d in datafromJson:
            makedict(d["from"],d["to"],int( d["value"]))

        return HttpResponse(json.dumps( astar(fromCity,toCity)))
    
    return render(request,'home.html',{"name":'taaa'})

