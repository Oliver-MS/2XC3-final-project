import min_heap
from final_project_part1 import *


def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relax_count = {} #Counter to keep track of number of relaxations per node
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
        relax_count[node] = 0
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if relax_count[current_node] < k: # Check if max relaxations limit is reached
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
                    relax_count[neighbour] += 1 # Increment the counter for the relaxed node
            else:
                break
    return dist

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relax_count = {} #Counter to keep track of number of relaxations per node
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
        relax_count[node] = 0
    dist[source] = 0

    #Meat of the algorithm
    for i in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if relax_count[node] < k: # Check if max relaxations limit is reached
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node
                        relax_count[neighbour] += 1 # Increment the counter for the relaxed node
                else:
                    break
    return dist