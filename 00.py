import math
from math import sqrt
sites = {
    'Moscow': (550,  370),
    'London': (510,  510),
    'Paris': (480,  480),
}

distances = {}

for city1 in sites:
    for city2 in sites:
        if city1 != city2:
            x1, y1 = sites[city1]
            x2, y2 = sites[city2]
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            distances[f'{city1}-{city2}'] = distance

# заполнение словаря distances
for key, value in distances.items():
    print(key, value)
