class Reversort:
    def __init__(self):
        self.cost = 0
    
    def reverSort(self, arr):
        for i in range(len(arr)-1):
            j = arr.index(min(arr[i:]))
            self.cost += j - i + 1
            arr = arr[:i] + arr[i:j+1][::-1] + arr[j+1:]
        return self.cost

for i, _ in enumerate(range(int(input())), start=1):
    n = int(input())
    arr = list(map(int, input().split()))
    cost = Reversort().reverSort(arr)
    print(f"Case #{i}: {cost}")
