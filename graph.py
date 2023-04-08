from abc import ABC, abstractmethod

class Graph(ABC):
    #abstract weighted graph
    
    def __init__(self):
        self.adj = {}
        self.weights = {}
    
    def get_adj_nodes(self, node:int):
        return self.adj[node]
    
    def add_node(self, node:int):
        self.adj[node] = []
    
    def add_edge(self, start:int, end:int, w:float):
        #assumes start is already in graph, may break if we attempt to pass a node that doesn't already exist
        #assumes directed graph as a baseline, undirected graph would require further modification
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = w
    
    def get_num_of_nodes(self) -> int:
        return len(self.adj)
    
    def w(self, node:int) -> float:
        #unsure what this is supposed to do, maybe return the node's integer value?
        #should probably return float("inf") since the implication is that this graph is not weighted, should also take two nodes as input
        pass
    
    def are_connected(self, start:int, end:int) -> bool:
        if end in self.adj[start]:
            return True
        return False
    
    #def w(self, node1:int, node2:int):
    #    return float("inf")