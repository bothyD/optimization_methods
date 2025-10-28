def max_sum_steps(n, values):
    if n == 0:
        return 0
    elif n == 1:
        return values[0]
    elif n == 2:
        return max(values[0] + values[1], values[1])
 
    dp = [0] * n
    dp[0] = values[0]
    dp[1] = max(values[0] + values[1], values[1])
 
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2]) + values[i]
 
    return dp[-1]
 
 
with open("ladder.in", "r") as f:
    n = int(f.readline().strip())
    values = list(map(int, f.readline().strip().split()))
 
result = max_sum_steps(n, values)
 
with open("ladder.out", "w") as f:
    f.write(str(result) + "\n")