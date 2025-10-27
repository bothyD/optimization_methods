from typing import List, Tuple
from my_modules.Edge import Edge

def init_grpah() -> Tuple[int, int, int, List[Edge]]:
  
    start_peack: int = 0  
    # peaks: int = 5 
    # edges: int = 7 
    # graph: List[Edge] = [
    #     # example 1 from book
    #     Edge(0, 1, 25),
    #     Edge(0, 2, 15),
    #     Edge(0, 3, 7),
    #     Edge(0, 4, 2),
    #     Edge(1, 2, 6),
    #     Edge(2, 3, 4),
    #     Edge(3, 4, 3)

    peaks: int = 6 
    edges: int = 9 
    graph: List[Edge] = [
        # example 2 from book
        Edge(0, 1, 13),
        Edge(0, 2, 18),
        Edge(0, 3, 17),
        Edge(0, 4, 14),
        Edge(0, 5, 22),
        Edge(1, 2, 26),
        Edge(1, 4, 22),
        Edge(2, 3, 3),
        Edge(3, 5, 19)

    ]
    return peaks, edges, start_peack, graph