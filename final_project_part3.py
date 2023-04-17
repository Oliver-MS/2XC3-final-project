import csv
import london
import itertools
import pandas
import pickle
from final_project_part1 import *
from final_project_part2 import *
from matplotlib import pyplot as plt
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
pairsC=[]
counter=0
for p in pairs:

    start = time.time()
    a_path = a_star(graph, p[0], p[1], london.get_h(graph, p[1]))
    end = time.time()
    a_star_time = end - start
    a_star_times.append(a_star_time)

    start = time.time()
    d_path = dijkstra(graph, p[0], p[1])
    end = time.time()
    dijkstra_time = end - start
    dijkstra_times.append(dijkstra_time)

    sources.append(p[0])
    destinations.append(p[1])
    a_paths.append(a_path)
    d_paths.append(d_path)    
    pairsC.append(counter)
    counter+=1

#data = {'source': sources, 'destination': destinations, 'a_star_time': a_star_times, 'dijkstra_time': dijkstra_times, 'a_path': a_paths, 'd_path': d_paths}

file2 = open(r'part3data.pkl', 'rb')
data = pickle.load(file2)
file2.close()
a_star_faster = 0
dijkstra_faster = 0
dijkstra_cases=[]
a_star_lines=0
dijkstra_lines=0
for i in range(0, len(data['source'])):
    if data['a_star_time'][i] < data['dijkstra_time'][i]:
        a_star_faster += 1
        a_star_lines+=london.lines[data['source'][i]]
    else:
        dijkstra_faster += 1
        dijkstra_cases.append((data['source'][i], data['destination'][i]))
        dijkstra_lines+=london.lines[data['source'][i]]

total_cases = a_star_faster + dijkstra_faster
print("\n\nA* was faster in " + str(a_star_faster/total_cases*100) + "% of cases")
print("In these cases, the average total number of lines from the source was " + str(a_star_lines/a_star_faster))
print("Dijkstra was only faster in " + str(dijkstra_faster) + " cases out of " + str(total_cases) + " total cases.")
print("In these cases, the average total number of lines from the source was " + str(dijkstra_lines/dijkstra_faster))
for case in dijkstra_cases:
    print("Dijkstra was faster for " + str(case[0]) + " to " + str(case[1]))
    print(london.lines[case[0]])

plt.plot(pairsC, a_star_times, label="a_star")
plt.plot(pairsC, dijkstra_times, label="dijkstra")

plt.xlabel('Pairs')
plt.ylabel('Time to find shortest path')
plt.title('A* vs Dijkstra')
plt.legend()
plt.show()


