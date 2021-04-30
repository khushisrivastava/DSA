# cook your dish here
from collections import Counter

for _ in range(int(input())):
    n, w, wr = map(int, input().split())
    weights = Counter(list(map(int, input().split())))
    
    if w <= wr:
        print("YES")
        continue
    else:
        for x, i in weights.items():
            if i % 2 == 0:
                wr += x*i
        if w <= wr:
            print("YES")
        else:
            print("NO")