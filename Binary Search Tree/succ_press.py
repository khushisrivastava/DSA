class Node: 
    def __init__(self, key):
        self.key  = key
        self.left = None
        self.right = None

def insert(node , key):
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
 
    else:
        node.right = insert(node.right, key)
 
    return node

class SuccPress:
    def __init__(self):
        self.s = None
        self.p = None

    def findSucPre(self, root, key):
        if not root:
            return
        
        if root.key == key:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                self.p = temp
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                self.s = temp
        
        elif root.key > key:
            self.findSucPre(root.left, key)
        else:
            self.findSucPre(root.right, key)

root = None
root = insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

sol = SuccPress()
sol.findSucPre(root, 50)
if sol.p:
    print("Preccedor: ", sol.p.key)
else:
    print("Preccedor: None")
if sol.p:
    print("Succesor: ", sol.s.key)
else:
    print("Succesor: None")
