def count_knight_paths(N, M):
    # создаём таблицу N x M, заполненную нулями
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = 1  # стартовая клетка
 
    for i in range(N):
        for j in range(M):
            if i-2 >= 0 and j-1 >= 0:
                dp[i][j] += dp[i-2][j-1]
            if i-1 >= 0 and j-2 >= 0:
                dp[i][j] += dp[i-1][j-2]
 
    return dp[N-1][M-1] 
 
# values = ".cc."
# print(max_grass(values))
 
 
with open("knight.in", "r") as f:
    n, m = map(int, f.readline().strip().split())
 
 
result = count_knight_paths(n,m)
 
 
with open("knight.out", "w") as f:
    f.write(str(result) + "\n")