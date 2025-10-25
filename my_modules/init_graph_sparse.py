from typing import List, Tuple
from my_modules.Edge import Edge

def init_sparse_graph() -> Tuple[int, int, int, List[Edge]]:
    peaks: int = 10        
    edges: int = 14        
    start_peack: int = 0   

    # Храним только одно направление (ненаправленные рёбра)
    graph: List[Edge] = [
        Edge(0, 1, 1),
        Edge(1, 2, 7),
        Edge(2, 3, 4),
        Edge(3, 4, 9),
        Edge(4, 5, 3),
        Edge(5, 6, 6),
        Edge(2, 7, 10),
        Edge(7, 8, 8),
        Edge(8, 9, 11),
        Edge(1, 9, 2),
        Edge(0, 4, 12),
        Edge(3, 7, 5),
        Edge(5, 9, 3),
        Edge(6, 8, 9)
    ]

    return peaks, edges, start_peack, graph
