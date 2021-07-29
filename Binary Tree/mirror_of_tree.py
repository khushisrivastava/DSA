class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def mirror(root):
    if not root:
        return
    mirror(root.left)
    mirror(root.right)
    root.right, root.left = root.left, root.right

def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print (root.data, end = ' ')
        inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
inOrder(root)
print()
mirror(root)
inOrder(root)
