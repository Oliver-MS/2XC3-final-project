import csv
import london
import itertools
from final_project_part1 import *
from final_project_part2 import *
import time
alldata=[]
#slightly modified dijkstra's to include destination and return shortest path for ease of comparison
def dijkstra(G, source, dest):
    pred = {} #Predecessor dictionary
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node # add/update predecessor
    if dest not in pred:
        return None, None
    path = [dest]
    while path[-1] != source:
        path.append(pred[path[-1]])
    path.reverse()
    return pred, path


graph = london.create_tube_graph()

pairs = list(itertools.combinations(graph.adj.keys(), 2))

test = a_star(graph, 1, 15, london.get_h(graph, 15))[1]
test2 = dijkstra(graph, 1, 15)[1]
print(test)
print(test2)

sources=[]
destinations=[]
a_star_times=[]
dijkstra_times=[]
a_paths=[]
d_paths=[]

for p in pairs:
    #for each pair of nodes (s, d), run a_star and dijkstra and time each and store the results in a .svg file
    start = time.time()
    a_path = a_star(graph, p[0], p[1], london.get_h(graph, p[1]))[1]
    end = time.time()
    a_star_time = end - start
    start = time.time()
    d_path = dijkstra(graph, p[0], p[1])[1]
    end = time.time()
    dijkstra_time = end - start
    #store columns source, destination a_star_time, dijkstra_time in a dictionary to be written to a csv file
    sources.append(p[0])
    destinations.append(p[1])
    a_star_times.append(a_star_time)
    dijkstra_times.append(dijkstra_time)
    a_paths.append(a_path)
    d_paths.append(d_path)


