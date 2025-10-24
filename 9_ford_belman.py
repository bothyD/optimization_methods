import numpy as np
from typing import List
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.get_path import get_path
from my_modules.Edge import Edge

INF = np.inf

def solve_sparse(n: int, m: int, v: int, edges: List[Edge]):
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]
    ops = [0]  
    prev = [None] * n 

    for i in range(n - 1):
        d_next = d.copy()
        op_count = 0
        for edge in edges:
            a, b, w = edge.a, edge.b, edge.cost
            if d[a] != INF and d[a] + w < d_next[b]:
                d_next[b] = d[a] + w
                prev[b] = a  # только при обновлении
        d = d_next
        table.append(d.copy())
        ops.append(op_count)
    
    table_np = np.array(table)
    return table_np, ops, prev

def solve_dense(n: int, m: int, v: int, edges: List[Edge]):
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]
    ops = [0]
    adj = np.full((n, n), INF)
    prev = [None] * n

    for edge in edges:
        adj[edge.a][edge.b] = min(adj[edge.a][edge.b], edge.cost)
    
    for i in range(n - 1):
        d_next = d.copy()
        op_count = 0
        for u in range(n):
            for w in range(n):
                if d[u] != INF and adj[u][w] != INF and d[u] + adj[u][w] < d_next[w]:
                    op_count += 1
                    d_next[w] = d[u] + adj[u][w]
                    prev[w] = u
        d = d_next
        table.append(d.copy())
        ops.append(op_count)
    
    table_np = np.array(table)
    return table_np, ops, prev

def main():
    peaks, edges, start_peack, graph = init_grpah()   
    dense_table, dense_ops, prev_dens  = solve_dense(peaks, edges, start_peack, graph)
    sparse_table, sparse_ops, prev_sparse  = solve_sparse(peaks, edges, start_peack, graph)
    
    print("\nСравнение Dense vs Sparse по итерациям:")
    for i in range(dense_table.shape[0]):
        print(f"Итерация {i}: Dense {dense_table[i]} | Sparse {sparse_table[i]}")
    
    # print("\nСравнение числа операций по итерациям:")
    # for i in range(dense_table.shape[0]):
    #     print(f"Итерация {i}: Dense {dense_ops[i]} | Sparse {sparse_ops[i]}")
    final_distances = dense_table[-1].astype(int)

    print(prev_dens)
    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev_dens, t)}, расстояние = {final_distances[t]}")

    # draw_graph(graph)

if __name__ == '__main__':
    main()
