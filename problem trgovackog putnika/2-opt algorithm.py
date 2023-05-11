import math
import matplotlib.pyplot as plt
import random

# Najbliži komšija za svaki grad
def nearest_neighbor(cities):
    path = [0] 
    unvisited = set(range(1, len(cities)))
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distance(
            cities[path[-1]], cities[city]))
        path.append(nearest_city)
        unvisited.remove(nearest_city)
    return path

#  Računa ukupnu dužinu putanje koja prolazi kroz gradove navedene u path,
#  koristeći funkciju distance za izračunavanje rastojanja između gradova.
def path_length(path, cities):
    total_length = 0
    for i in range(len(path)):
        city_i = path[i]
        city_j = path[(i + 1) % len(path)]
        total_length += distance(cities[city_i], cities[city_j])
    return total_length

# Euklidova distanca
def distance(city_i, city_j):
    dx = city_i[0] - city_j[0]
    dy = city_i[1] - city_j[1]
    return math.sqrt(dx**2 + dy**2)


def two_opt(cities, max_iterations=100):
    # Pronađi početni put koristeći nearest neighbor heuristiku
    path = nearest_neighbor(cities)
    path = path + [path[0]]
    improvement = True
    iteration = 0
    # Petlja se ponavlja dok se poboljšanja mogu napraviti
    # i dok se ne dostigne maksimalan broj iteracija
    while improvement and iteration < max_iterations:
        improvement = False
        # Unutar trenutnog puta,
        # pronađi parove gradova koji se mogu zameniti
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1:
                    continue
                # Napravi novi put zamjenom dva grada
                new_path = path[:]
                new_path[i:j] = path[j - 1:i - 1:-1]
                # Izračunaj novu dužinu puta
                new_distance = path_length(new_path, cities)
                # Ako je nova dužina puta manja od trenutne,
                # ažuriraj put i postavi da je bilo poboljšanja
                if new_distance < path_length(path, cities):
                    path = new_path
                    improvement = True
        iteration += 1
    # Vrati put bez poslednjeg grada, i njegovu dužinu
    return path[:-1], path_length(path[:-1], cities)

# Nasumicni primjer
random.seed(1)  
cities = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(10)]

path, length = two_opt(cities)
print("Path:", path)
print("Length:", length)

path_coords = [cities[i] for i in path]
path_coords.append(path_coords[0])  

xs, ys = zip(*path_coords)

plt.scatter(xs, ys, color='blue')
plt.plot(xs, ys, color='red')

for i, city in enumerate(path):
    plt.annotate(str(city), xy=cities[city], xytext=(10, 5), textcoords='offset points')

plt.show()
