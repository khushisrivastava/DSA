class Node:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

def inorderTree(root, arr):
    if not root:
        return 
    inorderTree(root.left, arr)
    arr.append(root)
    inorderTree(root.right, arr)

def buildUtil(arr, start, end):
    if start > end:
        return None
    
    mid = (start+end)//2
    node = arr[mid]
    node.left = buildUtil(arr, start, mid-1)
    node.right = buildUtil(arr, mid+1, end)
    return node

def buildTree(root):
    arr = []
    inorderTree(root, arr)

    return buildUtil(arr, 0, len(arr)-1)

def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)
root = buildTree(root)
print("Preorder traversal of balanced BST is :")
preorder(root)
