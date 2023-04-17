from graph import Graph


class WeightedGraph(Graph):

    def __init__(self):
        super().__init__()
        
    def get_nodes(self):
        return self.adj
    
    def get_adj_nodes(self, node:int):
        return self.adj[node]
    
    def add_node(self, node:int):
        self.adj[node] = []
    
    def add_edge(self, start:int, end:int, w:float):
        if end not in self.adj[start]:
            self.adj[start].append(end)
        if start not in self.adj[end]:
            self.adj[end].append(start)
        self.weights[(start, end)] = w
        self.weights[(end, start)] = w
    
    def get_num_of_nodes(self) -> int:
        return len(self.adj)
    
    def w(self, node1:int, node2:int) -> float:
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]
    
    def are_connected(self, start:int, end:int) -> bool:
        if end in self.adj[start]:
            return True
        return False