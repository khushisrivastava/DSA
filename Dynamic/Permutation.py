def permutation(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = i*dp[i-1][j-1]
    print(dp[n][k])

permutation(10, 11)