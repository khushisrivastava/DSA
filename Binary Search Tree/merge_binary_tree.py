class Node:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val == val:
        return root
    elif root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    return root

def inorder(root, arr):
    if not root:
        return
    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)

def mergeArr(arr1, arr2):
    i = 0
    j = 0
    arr = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

def arrToBST(arr, start, end):
    if not arr:
        return None
    if start > end:
        return None

    mid = (start+end) //2
    root = Node(arr[mid])
    root.left = arrToBST(arr, start, mid-1)
    root.right = arrToBST(arr, mid+1, end)
    return root

root1 = root2 = None
root1 = insert(root1, 100)
root1 = insert(root1, 50)
root1 = insert(root1, 300)
root1 = insert(root1, 20)
root1 = insert(root1, 70)
root2 = insert(root2, 80)
root2 = insert(root2, 40)
root2 = insert(root2, 120)

t1 = []
inorder(root1, t1)
t2 = []
inorder(root2, t2)

arr = mergeArr(t1, t2)
root = arrToBST(arr, 0, len(arr)-1)
t = []
inorder(root, t)
print(*t)
