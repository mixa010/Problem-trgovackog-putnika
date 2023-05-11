import heapq  

def nearest_neighbor(graph, start):
    # Kreiranje skupa neposećenih čvorova
    unvisited = set(graph.keys())
    # Označavanje početnog čvora kao posećenog i uklanjanje iz skupa
    current = start
    unvisited.remove(current)
    # Inicijalizacija liste posećenih čvorova početnim čvorom
    visited = [current]
    # Inicijalizacija prioritetnog reda sa komšijama početnog čvora
    pq = [(distance, neighbor) for neighbor,
          distance in graph[current].items() if neighbor in unvisited]
    heapq.heapify(pq)  # Pretvaranje liste u prioritetni red
    while pq:
        # Uzimanje najbližeg neposećenog čvora iz prioritetnog reda
        _, nearest = heapq.heappop(pq)
        # Ako je najbliži čvor neposećen, obrađujemo ga
        if nearest in unvisited:
            # Označavanje najbližeg čvora kao posećenog i uklanjanje iz skupa
            current = nearest
            unvisited.remove(current)
            # Dodavanje najbližeg čvora u listu posećenih čvorova
            visited.append(current)
            # Dodavanje suseda trenutnog čvora u prioritetni red
            for neighbor, distance in graph[current].items():
                if neighbor in unvisited:
                    heapq.heappush(pq, (distance, neighbor))
    # Dodavanje početnog čvora na kraj liste posećenih čvorova
    visited.append(start)
    return visited

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25},
    'B': {'A': 10, 'C': 8, 'D': 12, 'E': 16},
    'C': {'A': 15, 'B': 8, 'D': 6, 'E': 10},
    'D': {'A': 20, 'B': 12, 'C': 6, 'E': 4},
    'E': {'A': 25, 'B': 16, 'C': 10, 'D': 4}
}

path = nearest_neighbor(graph, 'A')
print(path)
