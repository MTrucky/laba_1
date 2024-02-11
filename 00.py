import math

sites = {
    'Moscow': (550,  370),
    'London': (510,  510),
    'Paris': (480,  480),
}

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2) **  2 + (y1 - y2) **  2)

distances = {}
for city1, coords1 in sites.items():
    distances[city1] = {}
    for city2, coords2 in sites.items():
        if city1 != city2:
            distance = calculate_distance(coords1, coords2)
            distances[city1][city2] = distance

print(distances)
