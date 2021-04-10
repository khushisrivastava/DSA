for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    ope = 0

    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            x[i] = int(str(x[i]) + '0')
            ope += 1
        elif x[i] < x[i-1]:
            diff_len = len(str(x[i-1])) - len(str(x[i]))
            if int(str(x[i])[0]) >= int(str(x[i-1])[0]):
                ope += diff_len
                x[i] = int(str(x[i]) + '0'*diff_len)
                x[i] += x[i-1] - x[i] + 1
            else:
                ope = ope + diff_len + 1
                x[i] = int(str(x[i]) + '0'*(diff_len+1))
            if x[i] < x[i-1]:
                x[i] = int(str(x[i]) + '0')
                ope += 1
            
    print(f"Case #{t+1}: {ope}") 
