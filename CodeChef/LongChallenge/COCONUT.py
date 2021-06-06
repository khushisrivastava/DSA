# cook your dish here
for _ in range(int(input())):
    xa, xb, Xa, Xb = map(int, input().split())
    
    a = Xa/xa
    b = Xb/xb
    
    print(int(a+b))