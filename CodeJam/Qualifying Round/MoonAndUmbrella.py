for p, _ in enumerate(range(int(input())), start=1):
    x, y, s = input().split()
    x = int(x)
    y = int(y)
    cost = 0
    i = 0

    while(i < len(s)):
        t = s[i]
        if i == 0: prev = None
        else: prev = s[i-1]
        if i == len(s) - 1: nex = None
        else: nex = s[i+1]
        
        if t == 'C':
            if nex == 'J': cost += x 
            elif nex == '?':
                i += 1
                while (i < len(s) and s[i] == '?'): i += 1
                if i >= len(s): new = t
                else: new = s[i]
                if t != new: cost += x
                continue     
        elif t == 'J':
            if nex == 'C': cost += y
            elif nex == '?': 
                i += 1
                while (i < len(s) and s[i] == '?'): i += 1
                if i >= len(s): new = t
                else: new = s[i]
                if t != new: cost += y
                continue
        i += 1
    
    print(f"Case #{p}: {cost}")