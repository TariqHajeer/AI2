import heapq


# city node for store city name and there distance
class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


class map:
    def __init__(self):
        self.rmap = {}

    def mkdir(self, city1, city2, distance):
        # check if distance greater than zero
        if(int(distance) > 0):
            # add city as key of object  and push a the other city and the distance from city1 to city2
            self.rmap.setdefault(city1, []).append(ctNode(city2, distance))


# a queue to store city depend on there cost
class priorityQueue:
    def __init__(self):
        self.cities = []
    # sotre city dened on there cost

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    # get name of first city depend on there cost

    def pop(self):
        return heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if (self.cities == []):
            return True
        else:
            return False


def astar(start, end, map: map):
    # create an object to stor path
    path = {}
    # create an object to store the distance of each city
    distance = {}

    q = priorityQueue()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    while (q.isEmpty() == False):
        current = q.pop()
        # if current path equal for end path
        if (current == end):
            break
        # if city don't let me access to other cities
        # skip this case
        if(current not in map.rmap):
            continue
        # check fore each city that the current city let me access to it
        for new in map.rmap[current]:
            # get cost for this city and added to privouse costs
            g_cost = distance[current] + int(new.distance)
            # if i don't visit this city before or the total cost less thant the cost of this city in the prviouse visit
            if (new.city not in distance or g_cost < distance[new.city]):
                # add the cost to distance by key named by city name
                distance[new.city] = g_cost
                # add for queue city and the final distance
                q.push(new.city, g_cost)
                # set the path of the new city is the current city
                path[new.city] = current
                # if the final path sould be like this A=>B=>Z
                # then it well be sotre like this {"B":"A","Z","B"}
    return output(start, end, path, distance)


#get the output 
def output(start, end, path, distance):

    if(end not in distance):
        return {"path": ["not found"], "totalDistance": "not found"}
    finalpath = []
    i = end
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    return {"path": finalpath, "totalDistance": str(distance[end])}
