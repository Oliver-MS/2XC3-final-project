from sp_algorithm import SPAlgorithm
import min_heap
#interesting question: does each implementation of SPAlgorithm have to import Graph or is there a fix to this?

class Bellman_Ford(SPAlgorithm):
    #this super needs fixing FYI
    def calc_sp(G, source, dest):

        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        nodes = list(G.adj.keys())

        #Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        #Meat of the algorithm
        for _ in range(G.number_of_nodes()):
            for node in nodes:
                for neighbour in G.adj[node]:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node
        if dest not in pred:
            return None, None
        path = [dest]
        while path[-1] != source:
            path.append(pred[path[-1]])
        path.reverse()
        return dist[dest]