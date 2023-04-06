class Graph():
    
    def __init__(self):
        self.adj = {}
        self.weights = {}
    
    def get_adj_nodes(self, node:int):
        return self.adj[node]
    
    def add_node(self, node:int):
        self.adj[node] = []
    
    def add_edge(self, start:int, end:int, w:float):
        #assumes start is already in graph, may break if we attempt to pass a node that doesn't already exist
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = w
    
    def get_num_of_nodes(self):
        return len(self.adj)
    
    def w(self, node:int):
        #unsure what this is supposed to do, maybe return the node's integer value?
        pass