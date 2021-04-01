import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

s = input()
s_bin = 0
for i in s:
    s_bin += ord(i)
print(s_bin)
print(isFibonacci(int(s_bin)))