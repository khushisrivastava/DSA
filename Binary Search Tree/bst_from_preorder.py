class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class ConstrustTree:
    def __init__(self, pre):
        self.pre = pre
        self.index = 0

    def construstTree(self, imin=float("-inf"), imax=float("inf")):
        if self.index >= len(self.pre):
            return None
        
        key = self.pre[self.index]
        root = None

        if key < imax and key > imin:
            root = Node(key)
            self.index += 1

            if self.index < len(self.pre):
                root.left = self.construstTree(imin, key)
            if self.index < len(self.pre):
                root.right = self.construstTree(key, imax)
        return root
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)


pre = [10, 5, 1, 7, 40, 50]
sol = ConstrustTree(pre)
root = sol.construstTree()
 
print("Inorder traversal of the constructed tree: ")
sol.inorder(root)
