class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def find_path(root, path, n):
    if not root:
        return False
    
    path.append(root.data)
    if root.data == n:
        return True

    if (root.left and find_path(root.left, path, n)) or (root.right and find_path(root.right, path, n)):
        return True
    
    path.pop()
    return False

def distance(root, n1, n2):
    if not root:
        return 0
    
    p1 = []
    find_path(root, p1, n1)
    p2 = []
    find_path(root, p2, n2)

    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] != p2[i]:
            break
        i += 1
    
    return len(p1) + len(p2) - 2*i

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)
 
dist = distance(root, 4, 5)
print ("Distance between node {} & {}: {}".format(4, 5, dist))
 
dist = distance(root, 4, 6)
print ("Distance between node {} & {}: {}".format(4, 6, dist))
 
dist = distance(root, 3, 4)
print ("Distance between node {} & {}: {}".format(3, 4, dist))
 
dist = distance(root, 2, 4)
print ("Distance between node {} & {}: {}".format(2, 4, dist))
 
dist = distance(root, 8, 5)
print ("Distance between node {} & {}: {}".format(8, 5, dist))
