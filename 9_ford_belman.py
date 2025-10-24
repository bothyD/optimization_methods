import numpy as np
from typing import List
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.Edge import Edge

INF = np.inf

def solve_sparse(n: int, m: int, v: int, edges: List[Edge]):
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]  
    for i in range(n - 1):
        d_next = d.copy()
        for edge in edges:
            a, b, w = edge.a, edge.b, edge.cost
            if d[a] != INF:
                d_next[b] = min(d_next[b], d[a] + w)
        d = d_next
        table.append(d.copy())
    
    table_np = np.array(table)
    return table_np

def solve_dense(n: int, m: int, v: int, edges: List[Edge]):
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]
    adj = np.full((n, n), INF)
    for edge in edges:
        adj[edge.a][edge.b] = min(adj[edge.a][edge.b], edge.cost)
    
    for i in range(n - 1):
        d_next = d.copy()
        for u in range(n):
            for w in range(n):
                if d[u] != INF and adj[u][w] != INF:
                    d_next[w] = min(d_next[w], d[u] + adj[u][w])
        d = d_next
        table.append(d.copy())
    table_np = np.array(table)
    return table_np

def main():
    peaks, edges, start_peack, graph = init_grpah()   
    dense_table = solve_dense(peaks, edges, start_peack, graph)
    sparse_table = solve_sparse(peaks, edges, start_peack, graph)
    
    print("\nСравнение Dense vs Sparse по итерациям:")
    for i in range(dense_table.shape[0]):
        print(f"Итерация {i}: Dense {dense_table[i]} | Sparse {sparse_table[i]}")
    draw_graph(graph)

if __name__ == '__main__':
    main()
