from abc import ABC, abstractmethod


class Graph(ABC):
    #abstract weighted graph
    
    def __init__(self):
        self.adj = {}
        self.weights = {}
    
    @abstractmethod
    def get_adj_nodes(self, node:int):
        pass
    
    @abstractmethod
    def add_node(self, node:int):
        pass
    
    @abstractmethod
    def add_edge(self, start:int, end:int, w:float):
        pass
    
    @abstractmethod
    def get_num_of_nodes(self) -> int:
        pass
    
    @abstractmethod
    def w(self, node1:int, node2:int) -> float:
        pass