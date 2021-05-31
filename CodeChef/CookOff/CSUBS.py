# cook your dish here
from collections import defaultdict

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    
    i = 0
    while (k+i <= n):
        sub_sum = sum(a[i:k+i])
        d[sub_sum] += 1
        i += 1

    sor = sorted(d.items(), key = lambda x: x[1])
    sor.pop()
    ans = 0
    for i in sor:
        ans += i[1]
    print(ans)