import itertools
    
def reverSort(n, c):
    for j in itertools.permutations(range(1, n+1)):
        arr = list(j)
        temp = arr
        cost = 0
        for i in range(len(arr)-1):
            j = arr.index(min(arr[i:]))
            cost += j - i + 1
            arr = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
        if cost == c:
            return " ".join(map(str, temp))
    return "IMPOSSIBLE"

for i, _ in enumerate(range(int(input())), start=1):
    n, c = map(int, input().split())
    res = reverSort(n, c)
    print(f"Case #{i}: {res}") 
    