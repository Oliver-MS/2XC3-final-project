from weighted_graph import WeightedGraph

#I don't think this is right but idrk what I'm doing
class HeuristicGraph(WeightedGraph):
    
    def __init__(self):
        super().__init__()
        self.heuristic = {}
        
    def get_heuristic(self):
        return self.heuristic