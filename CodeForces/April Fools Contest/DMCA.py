import math

s = int(input())
root = math.sqrt(s)
if root.is_integer():
    print(int(root))
else:
    print(root)