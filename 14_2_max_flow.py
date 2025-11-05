from my_modules.init_graph_for_flow import init_graph_from_file
from typing import  Tuple
import pandas as pd
import math

def printMatrix(peaks:int, masC:list[list[int]]):
    for i in range(1,peaks+1):
            for j in range(1, peaks+1):
                print(masC[i][j], end='\t')
            print()

# вывод итоговых путей
def printResultPath(listResPath:list[str]):
    for i in range(0, len(listResPath)):
        print(f'Итерация#{i+1}:{listResPath[i]}')

# табличка с потоками по рёбрам
def printRestable(peaks:int, masFlowData:list, graph:list):
    columnsName = ['Ребро','(Cij, Cji) - (cij, cji)','Величина потока',' Направление']
    DataRes = []
    c = init_flow_matrix(peaks, graph)
    for edge in graph:
        DataEl = []
        DataEl.append(f'({edge.a},{edge.b})') # Ребро
        DataEl.append(f'({edge.cost},{edge.flow})-' # (Cij, Cji)
                      f'({masFlowData[edge.a][edge.b][0]},{masFlowData[edge.a][edge.b][1]})=' # (cij, cji)
                      f'({edge.cost-masFlowData[edge.a][edge.b][0]},{edge.flow-masFlowData[edge.a][edge.b][1]})')
        DataEl.append(f'{edge.cost-masFlowData[edge.a][edge.b][0]}')  # Величина потока
        DataEl.append(f'{edge.a} -> {edge.b}') # Направление
        DataRes.append(DataEl)
    df = pd.DataFrame(data=DataRes, columns=columnsName)
    print(df.to_string(index=False))

# запись ребёр в матрицу
def init_flow_matrix(peaks:int, graph:list) -> list:
    masC = [[[0,0,1] for _ in range(peaks+1)] for _ in range(peaks+1)]
    for edge in graph:
        masC[edge.a][edge.b] = [edge.cost, edge.flow, 1]
        masC[edge.b][edge.a] = [edge.cost, edge.flow, -1]
    return masC

# получить доступные для перехода вершины
def get_enable_peaks(cur_peak:int, peaks:int, masC:list) -> Tuple[set, bool]:
    s = set()
    for i in range(cur_peak, peaks+1):
        if masC[cur_peak][i] > 0:
            s.add(i)
    if len(s) > 0:
        return s, True    
    for i in range(1, cur_peak):    
        if masC[cur_peak][i] > 0:
            s.add(i)
    return s, False

# поиск максимального ребра для перехода
def step_three(S:set, cur_point:int, masC:list) -> Tuple[int, int]:
    maxNext = -1
    indexEl = -1
    for el in S:
        if masC[cur_point][el]> maxNext:
            maxNext = masC[cur_point][el]
            indexEl=el
    return maxNext, indexEl

# поиск значения минимального ребра в пути
def get_max_flow_for_path(T:list) -> int:
    w = [x[0] for x in T]
    return min(*w)

# обновить матрицы потоков после итерации
def updateMasC(masC:list,  listWithPath:list, max_flow:int):
    for el in listWithPath:
        if el[1] == -1:
            continue
        sgn = masC[el[2]][el[1]][2]

        masC[el[1]][el[2]][0] -= max_flow * sgn
        masC[el[1]][el[2]][1] += max_flow * sgn

        masC[el[2]][el[1]][0] -= max_flow * sgn
        masC[el[2]][el[1]][1] += max_flow * sgn


# получить индекс следующей вершины
def get_max_peak(curInd:int, masC:list[list[int]], S:set)->int:
    m = 0
    v = -1
    for i, w in enumerate(masC[curInd]):

        if i in S:
            continue
        if w[2]==1:
            if m < w[0]:
                m=w[0]
                v=i
        else:
            if m<w[1]:
                m=w[1]
                v=i
    return v
def printListSteps(T:list[set]):
    print(f'поток|текущая вершина|прошлая вершина')
    res = ''
    for el in T:
        res+=f'{el}->'
    print(res[:len(res)-2],'\n')
    

def solve_flow(peaks:int, edges:int, start_peack:int, last_peak:int, graph:list) -> Tuple[list[list[int]], list[str], list[int]]:
    iteration = 0
    resultSumFlow = []
    listResPath = []
    masC = init_flow_matrix(peaks, graph)

    Tinit = (math.inf, -1, start_peack)  
    
    j = start_peack
    while j != -1:
        visitedPeak = set()
        stringPath = f'->{start_peack}'
        iteration+=1
        print(f"----------------Итерация#{iteration}----------------")
        i = start_peack
        T = [Tinit] 
        S = {start_peack} 
        while i != last_peak: 
            
            print("текущая вершина:", i)
            print(f'посещённые вершины:{S}')
            j = get_max_peak(i, masC, S)
            if j == -1:
                if i==start_peack:
                    break
                else:
                    print(f'шаг назад {i}->{T[-1][2]}')
                    i= T.pop()[2]
                    continue
            c = masC[i][j][0] if  masC[i][j][2] == 1 else masC[i][j][1]      
            T.append((c,j,i))
            S.add(j) 
            printListSteps(T)
            if j == last_peak:
                resultSumFlow.append(get_max_flow_for_path(T))
                updateMasC(masC, T, resultSumFlow[-1])
                stringPath+=f'->{last_peak} | {resultSumFlow[-1]}'
                listResPath.append(stringPath)
                break
            
            i=j
            stringPath+=f'->{j}'

    print('Все пути найдены\n')
    return masC, listResPath, resultSumFlow



def main():
    peaks, edges, start_peack,last_peak, graph = init_graph_from_file()
    masFlowData, listResPath, resultSumFlow = solve_flow(peaks, edges, start_peack,last_peak, graph)
    printRestable(peaks, masFlowData, graph)
    printResultPath(listResPath)
    print('общий поток = ', resultSumFlow, '=', sum(resultSumFlow))

if __name__=='__main__':
    main()