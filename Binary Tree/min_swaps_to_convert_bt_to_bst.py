def inorder(a, v, index):
    if index >= len(a):
        return
    inorder(a, v, 2*index+1)
    v.append(a[index])
    inorder(a, v, 2*index+2)

def swap(arr):
    ans = 0
    temp = arr.copy()
    temp.sort()

    for i in range(len(arr)):
        if arr[i] != temp[i]:
            ans += 1
            interchange(arr, i, arr.index(temp[i]))
    return ans

def interchange(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

a = [ 5, 6, 7, 8, 9, 10, 11 ]
v = []
inorder(a, v, 0)
print(swap(v))
