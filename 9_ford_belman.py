import numpy as np
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.get_path import get_path
from my_modules.Edge import Edge

INF = np.inf

# ---------------- Sparse (разреженный граф) ----------------
def solve_sparse(n: int, m: int, v: int, edges: List[Edge]) -> Tuple[np.ndarray, List[int], List[int]]:
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]
    op_count = 0 
    prev = [None] * n 

    for i in range(n - 1):
        d_next = d.copy()
        op_count += 1
        for edge in edges:
            op_count += 1
            a, b, w = edge.a, edge.b, edge.cost
            # обновление a->b
            if d[a] != INF and d[a] + w < d_next[b]:
                d_next[b] = d[a] + w
                prev[b] = a
            # обновление b->a (для ненаправленного графа)
            if d[b] != INF and d[b] + w < d_next[a]:
                d_next[a] = d[b] + w
                prev[a] = b
        d = d_next
        table.append(d.copy())
    
    table_np = np.array(table)
    return table_np, op_count, prev

# ---------------- Dense (плотный граф) ----------------
def solve_dense(n: int, m: int, v: int, edges: List[Edge]) -> Tuple[np.ndarray, List[int], List[int]]:
    d = np.full(n, INF)
    d[v] = 0
    table = [d.copy()]
    op_count = 0
    prev = [None] * n
    adj = np.full((n, n), INF)

    # заполняем матрицу смежности, учитывая ненаправленность
    for edge in edges:
        adj[edge.a][edge.b] = min(adj[edge.a][edge.b], edge.cost)
        adj[edge.b][edge.a] = min(adj[edge.b][edge.a], edge.cost)

    for i in range(n - 1):
        op_count += 1
        d_next = d.copy()
        for u in range(n):
            op_count += 1
            for w in range(n):
                op_count += 1
                if d[u] != INF and adj[u][w] != INF and d[u] + adj[u][w] < d_next[w]:
                    d_next[w] = d[u] + adj[u][w]
                    prev[w] = u
        d = d_next
        table.append(d.copy())

    table_np = np.array(table)
    return table_np, op_count, prev

# ---------------- Main ----------------
def main():
    peaks, edges, start_peack, graph = init_grpah()
    
    dense_table, dense_ops, prev_dense = solve_dense(peaks, edges, start_peack, graph)
    sparse_table, sparse_ops, prev_sparse = solve_sparse(peaks, edges, start_peack, graph)

    print("\nСравнение Dense vs Sparse по итерациям:")
    for i in range(dense_table.shape[0]):
        print(f"Итерация {i}: Dense {dense_table[i]} | Sparse {sparse_table[i]}")

    print("\n--- Трудоёмкость ---")
    print(f"Dense: теоретически O(V^3) = O({peaks**3})")
    print(f"Dense: практические операции  = {dense_ops}")
    print(f"Sparse: теоретически O(V*E) = O({peaks}*{len(graph)}) = {peaks*len(graph)}")
    print(f"Sparse: практические операции= {sparse_ops}")

    final_distances = dense_table[-1].astype(int)
    for t in range(peaks):
        print(f"Кратчайший путь до вершины {t}: {get_path(prev_dense, t)}, расстояние = {final_distances[t]}")
    # draw_graph(graph)

if __name__ == '__main__':
    main()
