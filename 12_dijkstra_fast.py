import numpy as np
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.init_graph_sparse import init_sparse_graph
from my_modules.build_adjacency_list import build_adj_list
from my_modules.get_path import get_path
from my_modules.Edge import Edge
import heapq

INF = np.inf

def dijkstra_fast(n: int, startPoint: int, edges: List[Edge], undirected: bool = True) -> Tuple[List[float], List[int], int]:
    adj = build_adj_list(n, edges, undirected=undirected)

    distance = [INF] * n
    distance[startPoint] = 0
    prev = [None] * n
    visitedPoints = []
    heapq.heappush(visitedPoints, (0, startPoint))

    operation_count = 0

    while visitedPoints:
        dist, curPoint = heapq.heappop(visitedPoints)
        operation_count += 1

        if dist != distance[curPoint]:
            continue

        for neighbor, cost in adj[curPoint]:
            operation_count += 1
            if distance[curPoint] + cost < distance[neighbor]:
                distance[neighbor] = distance[curPoint] + cost
                prev[neighbor] = curPoint
                heapq.heappush(visitedPoints, (distance[neighbor], neighbor))
                operation_count += 1

        print("Текущие расстояния:", distance)

    return distance, prev, operation_count


def main():
    peaks, edges, start_peack, graph = init_sparse_graph() 
    distance, prev, practical_ops = dijkstra_fast(peaks, start_peack, graph)
    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev, t)}, расстояние = {distance[t]}")
    
    
    
    # Теоретическая трудоемкость
    theoretical_complexity = f"O((V + E) * log V) = O(({peaks} + {len(graph)}) * log {peaks})"
    theoretical_complexity_res = (peaks + len(graph)) * np.log2(peaks)
    print(f"\nТеоретическая трудоемкость: {theoretical_complexity} = O({theoretical_complexity_res:.2f})")
    print(f"Практическая трудоёмкость: {practical_ops} элементарных операций")

    draw_graph(graph)  

if __name__ == '__main__':
    main()