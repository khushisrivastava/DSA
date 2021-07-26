def subsequence_product(a, k):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, len(a)+1):
            dp[i][j] = dp[i][j-1]

            if a[j-1] <= i:
                dp[i][j] += dp[i // a[j-1]][j-1] + 1
    return dp[k][len(a)]

A = [1,2,3,4]
k = 10

print(subsequence_product(A, k))
