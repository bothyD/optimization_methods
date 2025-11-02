import numpy as np
import pandas as pd
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.build_adjacency_list import build_adj_list
from my_modules.get_path import get_path
from my_modules.Edge import Edge

INF = np.inf


# глобальный список шагов
steps_data = []
def add_step(visited: list, current_point: int, dist_cur_point: int, dist: list):
    """Добавляет строку в общую таблицу шагов."""
    visited_nodes = [i for i, v in enumerate(visited) if v]
    row = {
        "S": str(visited_nodes),  # превращаем список в строку, чтобы красиво печатался
        "w": current_point,
        "D(w)": dist_cur_point,
    }
    for i, d in enumerate(dist):
        if visited[i+1] == True:
            row[f"D({i+1})"] = "-"
        else:
            row[f"D({i+1})"] = d  # сдвиг на +1, чтобы совпадало с твоим выводом D(1), D(2), ...
    steps_data.append(row)

def print_table():
    """Выводит все накопленные шаги одной таблицей."""
    df = pd.DataFrame(steps_data)
    print("\nРезультаты шагов алгоритма:\n")
    print(df.to_string(index=False))


def solve_dense(n: int, m: int, v: int, edges: List[Edge], undirected: bool = True) -> Tuple[List[float], List[int], int]:
    adj = build_adj_list(n, edges, undirected=undirected)
    distance = [INF] * n
    distance[v] = 0
    visited = [False] * n
    prev = [None] * n
    operation_count = 0  

    while True:
        u = -1
        min_dist = INF
        for i in range(n):
            operation_count += 1
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                u = i    
        

        if u == -1: 
            break  

        visited[u] = True  
        operation_count += 1
        # обновляем соседей
        for neighbor, cost in adj[u]:
            operation_count += 1
            if not visited[neighbor] and distance[u] + cost < distance[neighbor]:
                distance[neighbor] = distance[u] + cost
                prev[neighbor] = u
                operation_count += 1
        add_step(visited, u, min_dist, distance[1:])
        print_table()

    return distance, prev, operation_count


def main():
    peaks, edges, start_peack, graph = init_grpah() 
    distance, prev, practical_ops = solve_dense(peaks, edges, start_peack, graph)

    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev, t)}, расстояние = {distance[t]}")

    theoretical_complexity = f"O(V²) = O({peaks}²)"
    theoretical_complexity_res = peaks ** 2
    print(f"\nТеоретическая трудоёмкость: {theoretical_complexity} = {theoretical_complexity_res} операций")
    print(f"Практическая трудоёмкость: {practical_ops} элементарных операций")

    # draw_graph(graph)


if __name__ == '__main__':
    main()
