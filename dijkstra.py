from sp_algorithm import SPAlgorithm
from graph import Graph
import min_heap
#interesting question: does each implementation of SPAlgorithm have to import Graph or is there a fix to this?

class Dijkstra(SPAlgorithm):
    #this super needs fixing FYI
    def calc_sp(G, source, dest):
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