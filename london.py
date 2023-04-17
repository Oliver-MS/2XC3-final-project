import csv
import math

from heuristic_graph import HeuristicGraph

coords = {}
linesConnections = {}
lines = {}

def create_tube_graph() -> HeuristicGraph:
    tube_graph = HeuristicGraph()
    #coords = {station id: [latitude, longitude]}
    
    with open('csv_files/london_stations.csv', mode='r') as csvfile:
        tube_reader = csv.DictReader(csvfile)
        for line in tube_reader:
            tube_graph.add_node(int(line['id']))
            coords[int(line['id'])] = [float(line['latitude']), float(line['longitude'])]
            lines[int(line['id'])] = int(line['total_lines'])
    with open('csv_files/london_connections.csv', mode='r') as csvfile:
        connect_reader = csv.DictReader(csvfile)
        for line in connect_reader:
            s1 = int(line['station1'])
            s2 = int(line['station2'])
            line = int(line['line'])
            tube_graph.add_edge(s1, s2, calc_dist(coords[s1], coords[s2]))
            linesConnections[s1] = s2
    #the following are for testing and can be removed later:
    print(f"number of nodes: {tube_graph.get_num_of_nodes()}")
    print(f"weight between Charing Cross and Embankment (between 100m and 150m IRL): {calc_dist(coords[49], coords[87])}")
    return tube_graph
            
def calc_dist(p1, p2) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_h(G, t):
    to_return={}
    for node in G.adj.keys():
        to_return[node] = calc_dist(coords[node], coords[t])
    return to_return

#testing
s = create_tube_graph()
h = get_h(s, 49)
for test in h:
    print("Station: " + str(test) + " Distance: " + str(h[test]))
