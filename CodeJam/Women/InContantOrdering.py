for test in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    s = "A"
    for i in range(len(l)):
        if i%2 == 0:
            # Increasing
            if i != len(l) - 1 and l[i] < l[i+1]:
                diff = l[i+1] - l[i] + 1
            else:
                diff = 1
            s += "B"
            j = 1
            while j < l[i]:
                t = ord(s[-1]) if ord(s[-1])+diff <= 90 else 65-diff
                s += chr(t+diff) 
                j += 1
        else:
            # Decreasing
            if l[i-1] > l[i]:
                diff = l[i-1] - l[i] + 1
            else:
                diff = 1
            t = ord(s[-1]) if ord(s[-1])-diff >= 65 else 90+diff+1
            s += chr(t-diff)
            j = 1
            while j < l[i]:
                t = ord(s[-1]) if ord(s[-1])-1 >= 65 else 90+1
                s += chr(t-1)
                j += 1
    print(f"Case #{test+1}: {s}")
