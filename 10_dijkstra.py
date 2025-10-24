import numpy as np
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.get_path import get_path
from my_modules.Edge import Edge

INF = np.inf


def solve_dense(n: int, m: int, v: int, edges: List[Edge]) -> Tuple[List[int], List[int]]:
    distance = [INF] * n
    distance[v] = 0
    visited = [False] * n
    prev = [None] * n
    while True:
        # выбираем непосещённую вершину с минимальным distance
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i    
        if u == -1:  # все вершины посещены или недоступны
            break  
        visited[u] = True  
        # обновляем соседей
        for edge in edges:
            if edge.a == u and not visited[edge.b]:
                if distance[u] + edge.cost < distance[edge.b]:
                    distance[edge.b] = distance[u] + edge.cost
                    prev[edge.b] = u
        print("Текущие расстояния:", distance)
    return distance, prev
     

def main():
    peaks, edges, start_peack, graph = init_grpah() 
    distance, prev = solve_dense(peaks, edges, start_peack, graph)
    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev, t)}, расстояние = {distance[t]}")
    draw_graph(graph)

if __name__ == '__main__':
    main()