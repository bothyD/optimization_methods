def max_grass(s):
    n = len(s)
    dp = [-1] * n  
    dp[0] = 1 if s[0] == '"' else 0  
 
    for i in range(1, n):
        max_prev = -1
        for jump in [1, 3, 5]:  
            prev = i - jump
            if prev >= 0 and dp[prev] != -1:
                max_prev = max(max_prev, dp[prev])
        if max_prev == -1 or s[i] == 'w':  
            dp[i] = -1
        else:
            dp[i] = max_prev + (1 if s[i] == '"' else 0)
 
    return dp[-1]

 
with open("lepus.in", "r") as f:
    n = int(f.readline().strip())
    values = str(f.readline().strip())
 
result = max_grass(values)
 
with open("lepus.out", "w") as f:
    f.write(str(result) + "\n")