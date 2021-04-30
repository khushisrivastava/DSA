# cook your dish here
n = int(input())
a = sum(list(map(int, input().split())))
q = int(input())
x = list(input())

for i in range(q):
    a *= 2
    print(a%1000000007)