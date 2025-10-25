import numpy as np
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.get_path import get_path
from my_modules.Edge import Edge
import heapq

INF = np.inf

def dijkstra_fast(n: int,  startPoint:int, edges: List[Edge]) -> Tuple[List[float], List[int]]:
    distance = [INF]*n
    distance[startPoint] = 0
    prev=[None]*n
    visitedPoints = []
    heapq.heappush(visitedPoints, (0,startPoint))
    while visitedPoints:
        dist, curPoint = heapq.heappop(visitedPoints)
        if dist != distance[curPoint]:
            continue
        for edge in edges:
            if edge.a == curPoint:
                if distance[curPoint] + edge.cost < distance[edge.b]:
                    distance[edge.b]= distance[curPoint]+edge.cost
                    prev[edge.b]=curPoint
                    heapq.heappush(visitedPoints, (distance[edge.b], edge.b))
        print("Текущие расстояния:", distance)
    return distance, prev 


def main():
    peaks, edges, start_peack, graph = init_grpah() 
    distance, prev = dijkstra_fast(peaks, start_peack, graph)
    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev, t)}, расстояние = {distance[t]}")
    draw_graph(graph)  

if __name__ == '__main__':
    main()