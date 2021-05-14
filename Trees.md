# <center>**Trees**
<br>

## **Tree Data Structure:**
Non hierarchial data structure that consists of nodes and edges.<br>
##### **WHY?**:<br>
- Other datastructure are linear, operations time complexity increases with size.<br>
- Tree is non-linear, allows quicker and easire access to data.
<br>

### Terminologies:
- **Node**: 
    - Entity that contains value and pointer to child nodes.
    - Last node of each path is called Leaf Node or external node. They do not have pointer to child.
    - Node having atleast one pointer to child node is called internal node.
- **Edge**: Link between two nodes.
- **Root**: Topmost element of the tree.
- **Height of the node**: Longest path from node to leaf node.
- **Depth of the node**: Number of edges from root to node.
- **Height of tree**: Longest path from root to leaf node (Height of root node).
- **Degree of node**: Number of branches of the node.
- **Forest**: Collection of disjoint trees.
<br>

### Types:
- Binary Tree
- Binary Search Tree
- Avial Tree
- B- Tree
<br>

### Applications:
- BST used to check if an element is present.
- Heaps used in heap sort.
- Tries used in routers to store routing information.
- Databases use B- and T- trees.
- Compilers use syntax trees to validate synatx of programs.

****************************************************************************
<br>
<br>

## **Tree Traversal:**
Traversing means visiting every node of the tree.

### Inorder Traversal:
- left -> root -> right
-  ```
    inorder(root->left)
    display(root->data)
    inorder(root->right)
<br>

### Preorder Traversal:
- root -> left -> right
- ```
    display(root->data)
    preorder(root->left)
    preorder(root->right)
<br>

### Postorder Traversal:
- left -> right -> root
- ```
    postorder(root->left)
    postorder(root->right)
    display(root->data)
<br>

### Implementation:
```python
# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)
```

****************************************************************************
<br>
<br>
