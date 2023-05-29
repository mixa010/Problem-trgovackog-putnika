import heapq
import time
import random
import networkx as nx
import matplotlib.pyplot as plt

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

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25},
    'B': {'A': 10, 'C': 8, 'D': 12, 'E': 16},
    'C': {'A': 15, 'B': 8, 'D': 6, 'E': 10},
    'D': {'A': 20, 'B': 12, 'C': 6, 'E': 4},
    'E': {'A': 25, 'B': 16, 'C': 10, 'D': 4}
}

path = nearest_neighbor(graph, 'A')

for n in [10, 15, 20]:
    graph = create_random_graph(n)
    G = nx.Graph(graph)
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

    # Oznaci najkraci put crvenom bojom
    shortest_path = [(path[i], path[i+1]) for i in range(len(path)-1)]
    other_edges = [(u, v) for u, v in G.edges() if (u, v) not in shortest_path and (v, u) not in shortest_path]
    
    nx.draw_networkx_edges(G, pos, edgelist=shortest_path, edge_color='red', width=2.0)
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='black', alpha=0.2)

    plt.title(f"n={n}")
    plt.axis('off')
    plt.show()

    start_time = time.time()
    path = nearest_neighbor(graph, 'A')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\n n={n} = {execution_time} sekundi")
    print(path)
