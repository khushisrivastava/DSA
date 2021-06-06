# cook your dish here
for _ in range(int(input())):
    D, d, p, q = map(int, input().split())
    
    if d >= D:
        print(D*p)
    else:
        cost = D*p
        complete_days = int(D//d)
        remaining_days = int(D%d)

        cost += int((complete_days*(complete_days-1))/2) * q * d
        cost += remaining_days * q * complete_days
        print(int(cost))
