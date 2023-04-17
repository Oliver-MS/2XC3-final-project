from graph import Graph
from abc import ABC, abstractmethod

#ABC inheritance specifies abstract class
class SPAlgorithm(ABC):
    #unsure if this needs an init function
    
    @abstractmethod
    def calc_sp(self, graph:Graph, source:int, dest:int) -> float:
        pass
        