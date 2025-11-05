from my_modules.init_graph_for_flow import init_graph_from_file
from typing import  Tuple
import pandas as pd


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
        DataEl.append(f'({edge.cost},{edge.flow})-'
                      f'({masFlowData[edge.a][edge.b]},{masFlowData[edge.b][edge.a]})='
                      f'({edge.cost-masFlowData[edge.a][edge.b]},{edge.flow-masFlowData[edge.b][edge.a]})')
        DataEl.append(f'{edge.cost-masFlowData[edge.a][edge.b]}')  # Величина потока
        DataEl.append(f'{edge.a} -> {edge.b}') # Направление
        DataRes.append(DataEl)
    df = pd.DataFrame(data=DataRes, columns=columnsName)
    print(df.to_string(index=False))

# запись ребёр в матрицу
def init_flow_matrix(peaks:int, graph:list) -> list:
    masC = [[-1 for _ in range(peaks+1)] for _ in range(peaks+1)]
    for edge in graph:
        masC[edge.a][edge.b] = edge.cost
        masC[edge.b][edge.a] = edge.flow
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
def get_max_flow_for_path(Np:list) -> int:
    min_value = float('inf') 
    for pair in Np:
        if pair != []:
            left_element = pair[0]
            if isinstance(left_element, int) and left_element < min_value:
                min_value = left_element

    return min_value if min_value != float('inf') else None

# обновить матрицы потоков после итерации
def updateMasC(masC:list, start_peack:int, last_peack:int, Np:list, max_flow:int):
    curEl = last_peack
    nextEl = -1
    while curEl != start_peack:
        nextEl = Np[curEl][1]
        masC[nextEl][curEl]-=max_flow
        masC[curEl][nextEl]+=max_flow
        curEl=nextEl

# проверка наличия путей из начальной точки
def isHaveEnablePath(start_peack:int, masC:list)-> bool:
    print('isHaveEnablePath - ', masC[start_peack])
    for i in range(len(masC[start_peack])):

        if masC[start_peack][i]>0:
            return True
    return False



def solve_flow(peaks:int, edges:int, start_peack:int, graph:list) -> Tuple[list[list[int]], list[str], int]:
    iteration = 0
    resultSumFlow = 0
    listResPath = []
    masC = init_flow_matrix(peaks, graph)
    while(isHaveEnablePath(start_peack, masC)):
        visitedPeak = set()
        stringPath = f'->{start_peack}'
        iteration+=1
        print(f"----------------Итерация#{iteration}----------------")
        # step 1
        i = start_peack
        Np = [[] for _ in range(peaks+1)]
        Np[1] = ('inf', '-')
        while i !=peaks: 
            # step 2
            print('\tstep 2')
            S, isGoToUp = get_enable_peaks(i, peaks, masC)
            print(f'S - visitedPeak =  {S}-{visitedPeak}={S-visitedPeak}')
            S -= visitedPeak 
            
            if len(S) != 0:
                # step 3
                print('\tstep 3')
                nextDist, nextPeak = step_three(S, i, masC)
                Np[nextPeak] = ((nextDist, i))
                visitedPeak.add(i)
                i = nextPeak
                stringPath+= f'->{i}'
            else:
                # step 4
                print('\tstep 4')
                curI = i 
                visitedPeak.add(i)
                i = Np[i][1]
                Np[curI] = []
                stringPath+= f'->{i}'

            print(Np)
            
        # step 5
        print('\tstep 5')
        max_flow = get_max_flow_for_path(Np)
        resultSumFlow+=max_flow
        stringPath+=f' | поток {max_flow}'
        # print(max_flow)
        updateMasC(masC, start_peack, peaks, Np, max_flow)
        print(stringPath)
        listResPath.append(stringPath)

    return masC, listResPath, resultSumFlow


def main():
    peaks, edges, start_peack, graph = init_graph_from_file()
    masFlowData, listResPath, resultSumFlow = solve_flow(peaks, edges, start_peack, graph)
    printRestable(peaks, masFlowData, graph)
    printResultPath(listResPath)
    print('общий поток = ', resultSumFlow)

if __name__=='__main__':
    main()