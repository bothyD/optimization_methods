from typing import List, Tuple
from my_modules.Edge import Edge

def init_grpah() -> Tuple[int, int, int, List[Edge]]:
    peaks: int = 5  # Количество вершин
    edges: int = 7  # Количество рёбер
    start_peack: int = 0  # Начальная вершина
    graph: List[Edge] = [
        Edge(0, 1, 25),
        
        Edge(0, 2, 15),

        Edge(0, 3, 7),

        Edge(0, 4, 2),

        Edge(1, 2, 6),

        Edge(2, 3, 4),

        Edge(3, 4, 3)
    ]
    return peaks, edges, start_peack, graph
