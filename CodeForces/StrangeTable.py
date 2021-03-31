for _ in range(int(input())):
    n, m, x = map(int, input().split())

    for i, j in enumerate(range(n,n*m+1, n)):
        if x <= j:
            c = i
    for i, j in enumerate(range((n*m+1)-n,n*m+1)):
        if x <= j:
            r = i
    print(abs(r*m + c+1))