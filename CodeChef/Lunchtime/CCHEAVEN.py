# cook your dish here
for _ in range(int(input())):
    l = int(input())
    s = list(input())

    zero = 0
    one = 0

    t = True
    
    for i in s:
        if i == "0": zero += 1
        else: one += 1

        if one >= zero: t = False

    if t:
        print("NO")
    else:
        print("YES")