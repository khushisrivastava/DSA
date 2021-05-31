# cook your dish here
for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    
    dis = abs(a-c) + abs(b-d)
    
    if (dis%2 == 0 and k%2 == 0) or (dis%2 == 1 and k%2 == 1):
        print("YES")
    else:
        print("NO")