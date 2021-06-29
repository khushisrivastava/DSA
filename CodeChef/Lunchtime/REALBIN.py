# cook your dish here
from datetime import datetime

start = datetime.now()
for _ in range(int(input())):
    a, b = map(int, input().split())
    
    if b%2 == 0:
        print("Yes")
    else:
        print("No")
    
stop = datetime.now()
print(stop-start)