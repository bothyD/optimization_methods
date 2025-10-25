from typing import List, Tuple
from my_modules.Edge import Edge

def build_adj_list(n: int, edges: List[Edge], undirected: bool = True) -> List[List[Tuple[int,int]]]:
    """Создаёт список смежности. Если undirected=True — добавляет обратные рёбра."""
    adj = [[] for _ in range(n)]
    for e in edges:
        adj[e.a].append((e.b, e.cost))
        if undirected:
            adj[e.b].append((e.a, e.cost))
    return adj