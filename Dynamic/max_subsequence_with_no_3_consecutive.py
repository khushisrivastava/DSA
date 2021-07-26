def max_seq(a):
    dp = [0] * len(a)

    if len(a) >= 1:
        dp[0] = a[0]
    if len(a) >= 2:
        dp[1] = a[0] + a[1]
    if len(a) > 2:
        dp[2] = max(dp[1], a[0]+a[2], a[1]+a[2])
    
    for i in range(3, len(a)):
        dp[i] = max(dp[i-1], (dp[i-2]+a[i]), (dp[i-3]+a[i]+a[i-1]))
    
    return dp[len(a)-1]

arr = [100, 1000, 100, 1000, 1]
print(max_seq(arr))