n = int(input().strip())
numbers = []
for el in range(n):
    numbers.append(list(map(int, input().strip().split())))

dp = [[float('-inf')] * len(numbers[i]) for i in range(len(numbers))]
dp[0][0] = numbers[0][0]

for i in range(n):
    for j in range(len(numbers[i])):
        if i+1<n:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + numbers[i+1][j])
        if i+1<n and (j+1 <= len(numbers[i])):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + numbers[i+1][j+1])
print(max(dp[-1]))