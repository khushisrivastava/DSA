class newNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printKpath(root, k, path=[]):
    if not root:
        return
    path.append(root.data)
    printKpath(root.left, k, path)
    printKpath(root.right, k, path)

    f = 0
    for i in range(len(path)-1, -1, -1):
        f += path[i]
        if f == k:
            print(*path[i:])
    path.pop()

root = newNode(1)
root.left = newNode(3)
root.left.left = newNode(2)
root.left.right = newNode(1)
root.left.right.left = newNode(1)
root.right = newNode(-1)
root.right.left = newNode(4)
root.right.left.left = newNode(1)
root.right.left.right = newNode(2)
root.right.right = newNode(5)
root.right.right.right = newNode(2)

k = 5
printKpath(root, k)
