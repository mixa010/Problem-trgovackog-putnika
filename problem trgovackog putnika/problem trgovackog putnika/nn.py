import heapq
import time
import random

def nearest_neighbor(graph, start):
    unvisited = set(graph.keys())
    current = start
    unvisited.remove(current)
    visited = [current]
    pq = [(distance, neighbor) for neighbor,
          distance in graph[current].items() if neighbor in unvisited]
    heapq.heapify(pq)
    while pq:
        _, nearest = heapq.heappop(pq)
        if nearest in unvisited:
            current = nearest
            unvisited.remove(current)
            visited.append(current)
            for neighbor, distance in graph[current].items():
                if neighbor in unvisited:
                    heapq.heappush(pq, (distance, neighbor))
    visited.append(start)
    return visited

def create_random_graph(n):
    graph = {}
    nodes = [chr(ord('A') + i) for i in range(n)]
    for node in nodes:
        graph[node] = {}
    
    for node in nodes:
        for neighbor in nodes:
            if node != neighbor:
                distance = random.randint(1, 100)
                graph[node][neighbor] = distance
    
    return graph


for n in [10, 100, 1000, 10000]:
    graph = create_random_graph(n)
    start_time = time.time()
    path = nearest_neighbor(graph, 'A')
    end_time = time.time()
    print(f"\nn={n} = {end_time - start_time} sekundi")
