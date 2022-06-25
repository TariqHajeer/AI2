import heapq


class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)


class map:
    def __init__(self):
        self.rmap = {}

    def mkdir(self, city1, city2, distance):
        if(int(distance) > 0):
            self.rmap.setdefault(city1, []).append(ctNode(city2, distance))

#FIFO
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


def astar(start, end, map: map):
    path = {}
    distance = {}
    q = priorityQueue()
    q.push(start, 0)
    distance[start] = 0
    path[start] = None

    while (q.isEmpty() == False):
        current = q.pop()

        if (current == end):
            break    
        if(current not in map.rmap):
            continue
        for new in map.rmap[current]:
            g_cost = distance[current] + int(new.distance)

            if (new.city not in distance or g_cost < distance[new.city]):
                distance[new.city] = g_cost
                f_cost = g_cost
                q.push(new.city, f_cost)
                path[new.city] = current
    return output(start, end, path, distance)


def output(start, end, path, distance):
    finalpath = []
    i = end
    if(end not in distance):
        return {"path":["not found"],"totalDistance":"not found"}
    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    return {"path": finalpath, "totalDistance": str(distance[end])}
