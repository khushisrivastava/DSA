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

## **Binary Tree:**
Tree in which each node has atmost 2 childern.

### Types:
- **Full Binary Tree**: Each node either has 2 child node or no child node.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/full-binary-tree_0.png" height="20%" width="20%" >

- **Perfect Binary Tree**: Each internal node has 2 child nodes and all leaf nodes are at same level. 
<img src="https://cdn.programiz.com/sites/tutorial2program/files/perfect-binary-tree_0.png" height="30%" width="30%" >

- **Complete Binary Tree**: Similar to Full Binary Tree but with few differences:
    - Every level must be completely filled.
    - Leaf element must lean towards left.
    - Last leaf node might not have right sibling.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree_0.png" height="30%" width="30%" >

- **Degenerate or Pathological Tree**: Tree having sigle child either left or right.
<img src="https://cdn.programiz.com/sites/tutorial2program/files/degenerate-binary-tree_0.png" height="20%" width="20%" >

- **Skewed Binary Tree**: Pathological Binary tree in which tree is either dominated by left nodes or the right nodes. Are of 2 types:
    - Left-Skewed Binary Tree
    - Right-Skewed Binary Tree

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/skewed-binary-tree_0.png" height="30%" width="30%" >

- **Balanced Binary Tree**: Type of Binary Tree in which the difference between the height of left and right sub tree for each node is either 1 or 0.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/height-balanced_1.png" height="35%" width="35%" >

****************************************************************************
<br>
<br>

## **Full Binary Tree:**
It is a binary tree in which every internal node have either 2 chlid nodes or no child node.<br>
Known a **Proper Binary Tree**.

### Theorems:
`i` = number of internal nodes,<br>
`n` = total number of nodes,<br>
`l` = number of leaves,<br>
`λ` = number of levels
<br>
- Number if leves = `i+1`
- Total number of nodes = `2i+1`
- Number of internal nodes = `(n-1)/2`
- Number of leaves = `(n+1)/2`
- Total number of nodes = `2l-1`
- Number of internal nodes = `l-1`
- Number of leaves at most = `2^(λ - 1)`
<br>

### Implementation:
```python
# Creating a node
class Node:

    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None


# Checking full binary tree
def isFullTree(root):

    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
```

****************************************************************************
<br>
<br>
