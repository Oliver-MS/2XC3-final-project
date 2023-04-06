from graph import Graph

class WeightedGraph(Graph):
    
    def __init__(self):
        super().__init__(self)
        self.weights = {}
    
    def w(self, node1:int, node2:int):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]