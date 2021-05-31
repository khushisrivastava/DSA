# cook your dish here
for _ in range(int(input())):
    n = int(input())
    n_list = [ i for i in range(2, n+1)]
    groups = []
    final = []
    
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, n+1):
        if prime[p]:
            groups.append(list(range(p, n+1, p)))
    
    final.append(groups[0])
    
    for i in range(1, len(groups)):
        for f in range(0,len(final)):
            if set(final[f]).intersection(set(groups[i])):
                final[f].extend(groups[i])
            else:
                if groups[i] not in final: final.append(groups[i])
    
    print(len(final))
    