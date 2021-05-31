# cook your dish here
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    path = 0
    while (True):
        d = y1 + x1 - 1
        if x1==1 and y1==1:
            path += 1
            x1 += 1
            continue
        d_val = (d*(d-1))/2
        path += (d_val + x1)
        if x1 == x2: break
        else: x1 += 1

    y1 += 1
    while (True):
        d = y1 + (x1-1)
        if x1==1 and y1==1:
            path += 1
            y1 += 1
            continue
        d_val = (d*(d-1))/2
        path += (d_val+x1)
        if y1 == y2: break
        else: y1 += 1
    
    print(path)