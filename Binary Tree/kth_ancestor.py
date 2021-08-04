class newNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ancestor(root, node, k):
    if not root:
        return None
    if root.data == node and k == 0:
        return root
    if k <= 0:
        return None
    if ancestor(root.left, node, k-1) or ancestor(root.right, node, k-1):
        return root
    return None

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

k = 2
node = 5
parent = ancestor(root, node, k)
print(parent.data if parent else None)
