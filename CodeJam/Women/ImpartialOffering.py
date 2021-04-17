from collections import Counter

for t in range(int(input())):
    n = int(input())
    s = sorted(list(map(int, input().split())))

    od = Counter(s)
    treats = 0
    for i, x in enumerate(od, start=1):
        treats += i * od[x]
    print(f"Case #{t+1}: {treats}")
