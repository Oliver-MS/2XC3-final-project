from graph import Graph

class WeightedGraph(Graph):
    
    #makes sure graph is undirected
    def add_edge(self, start: int, end: int, w: float):
        if end not in self.adj[start]:
            self.adj[start].append(end)
        if start not in self.adj[end]:
            self.adj[end].append(start)
        self.weights[(start, end)] = w
        self.weights[(end, start)] = w
    
    def w(self, node1:int, node2:int) -> float:
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]