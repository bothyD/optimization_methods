from typing import Tuple
from my_modules.Edge import Edge

def init_graph_from_file(filename: str = r'my_modules\txt\graph3.txt') -> Tuple[int, int, int, list]:
    with open(filename, "r", encoding="utf-8") as f:
        peaks = int(f.readline().strip())
        edges = int(f.readline().strip())
        start_peak = int(f.readline().strip())
        last_peak = int(f.readline().strip())
        graph: list[Edge] = []
        for _ in range(edges):
            line = f.readline().strip()
            if not line:
                continue
            u, v, capacity = map(int, line.split())
            graph.append(Edge(u, v, capacity))

    return peaks, edges, start_peak, last_peak, graph
