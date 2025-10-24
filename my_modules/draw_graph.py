import networkx as nx
from typing import List
import matplotlib.pyplot as plt

from my_modules.Edge import Edge

def draw_graph(edges: List[Edge]):
    # G = nx.DiGraph()  # Направленный граф
    G = nx.Graph()    # Ненаправленный граф
    # Добавляем рёбра в граф
    for edge in edges:
        G.add_edge(edge.a, edge.b, weight=edge.cost)

    pos = nx.spring_layout(G)  # Позиции вершин
    labels = nx.get_edge_attributes(G, 'weight')  # Метки рёбер

    # Рисуем граф
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=16, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

    plt.title("Граф")
    plt.show()