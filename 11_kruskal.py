import numpy as np
from typing import List, Tuple
from my_modules.draw_graph import draw_graph
from my_modules.init_graph import init_grpah
from my_modules.build_adjacency_list import build_adj_list
from my_modules.get_path import get_path
from my_modules.Edge import Edge
from multiprocessing import Process

def kruskal_solve(edgesSorted: List[Edge])-> list:
    listConectedPeaks = set()
    dictSoloPeaks = {}
    resTree = []
    for el in edgesSorted:
        if el.a not in listConectedPeaks or el.b not in listConectedPeaks:
            if el.a not in listConectedPeaks and el.b not in listConectedPeaks:
                dictSoloPeaks[el.a] = [el.a, el.b]
                dictSoloPeaks[el.b] = dictSoloPeaks[el.a]
            else:
                if not dictSoloPeaks.get(el.a):
                    dictSoloPeaks[el.b].append(el.a)
                    dictSoloPeaks[el.a]=dictSoloPeaks[el.b]
                else:
                    dictSoloPeaks[el.a].append(el.b)
                    dictSoloPeaks[el.b]=dictSoloPeaks[el.a]
            resTree.append(el)
            listConectedPeaks.add(el.a)
            listConectedPeaks.add(el.b)
    for el in edgesSorted:
        if  el.b not in dictSoloPeaks[el.a]:
            resTree.append(el)
            gr1 = dictSoloPeaks[el.a]
            dictSoloPeaks[el.a] += dictSoloPeaks[el.b]
            dictSoloPeaks[el.b] += gr1
    
    return resTree

def main():
    peaks, edges, start_peack, graph = init_grpah()
    graphSorted= sorted(graph, key=lambda x:x.cost)
    res = kruskal_solve(graphSorted)
    for el in res:
        print(el.a,'<->', el.b,' cost: ',el.cost)

 
      # Создаем процессы для каждого графика
    p1 = Process(target=draw_graph, args=(graph,))
    p2 = Process(target=draw_graph, args=(res,))

    # Запускаем процессы
    p1.start()
    p2.start()

    # Ждем завершения процессов
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()