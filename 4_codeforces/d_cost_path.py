def find_small_path(mas_table):
    N = 8
    M = 8
    start_i,start_j=7,0
    dp = [[float('inf')] * M for _ in range(N)]
    dp[start_i][start_j]=mas_table[start_i][start_j]
    for i in range(start_i, start_j-1,-1):
        for j in range(start_i+1):
            if i+1<N:
                dp[i][j] = min(dp[i][j], dp[i+1][j] + mas_table[i][j]) 
            if j-1>=0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + mas_table[i][j])
            if i+1<N and j-1>=0:
                dp[i][j] = min(dp[i][j], dp[i+1][j-1] + mas_table[i][j])
 
    return dp[0][M-1]
 
 
with open("king2.in", "r") as f:
    mas_table = [list(map(int, f.readline().strip().split())) for _ in range(8)]
# print(mas_table)
 
result = find_small_path(mas_table)
 
 
with open("king2.out", "w") as f:
    f.write(str(result) + "\n")