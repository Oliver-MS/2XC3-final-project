from sp_algorithm import SPAlgorithm
from graph import Graph


class ShortPathFinder():
    
    def __init__(self, g:Graph, alg:SPAlgorithm) -> None:
        self.algorithm = alg
        self.graph = g
        
    def calc_short_path(self, source:int, dest:int) -> float:
        return self.algorithm.calc_sp(self.graph, source, dest)
    
    def set_graph(self, g:Graph):
        self.graph = g
    
    def set_algorithm(self, alg:SPAlgorithm) -> None:
        self.algorithm = alg