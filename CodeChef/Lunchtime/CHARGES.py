# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    charges = list(map(int, input().split()))

    i = 0
    ans = 0
    while (i < len(s)-1):
        if s[i] == s[i+1]:
            ans += 2
        else:
            ans += 1
        i += 1
    
    for q in charges:
        if s[q-1] == '1': s[q-1] = "0"
        else: s[q-1] = "1"
        
        if q-2 >= 0:
            if s[q-1] == s[q-2]: ans += 1
            else: ans -= 1
        if q < len(s):
            if s[q-1] == s[q]: ans += 1
            else: ans -= 1
        
        print(ans)