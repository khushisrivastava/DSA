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

## Perfect Binary Tree
Tree in which every internal node has exactly 2 child nodes and all leaf nodes are at same level.<br>
All internal nodes have `degree 2`.<br>
#### **Perfect Binary Tree is defined as**:
- Single node with no childern, `h=0`,
- Node has height `h>0`, and are prefect binary if both of its subtree has height `h-1` and are non- overlapping.
<br>

### Implementation:
```python
# Checking if a binary tree is a perfect binary tree in Python


class newNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


# Calculate the depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d


# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if (root is None):
        return True

    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))


root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

if (is_perfect(root, calculateDepth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
```
<br>

### Theorems:
- Prefect Binary tree of height `h` has `2^(h+1) -1` nodes.
- Prefect Binary tree with `n` nodes have height `log(n + 1) – 1 = Θ(ln(n))`.
- Perfect Binary tree of height `h` has `2^h` leaf nodes.
- Average depth of a node in perfect binary tree is `Θ(ln(n))`.

****************************************************************************
<br>
<br>

## **Complete Binary Tree:**
Binary tree in which all the levels are completely filled except for the lowest one, which is filled from left.

#### **Difference Between Full and Complete Binary Tree:**
- Leaf must lean towards left.
- Last leaf might not have right sibling.
<br>

### Creating Complete Binary Tree:
- 1st element of the list is choosen as the root node.
    
    <img src="https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree-creation-1.png" height="30%" width="30%" >
- 2nd element is put as the left child of the root and 3rd element is put as right child of the root.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree-creation-2.png" height="30%" width="30%" >
- Next 2 element is put as child node of the left node in second level and next 2 element after that is put as child node of right node.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/complete-binary-tree-creation-3.png" height="30%" width="30%" >
- Repeat untill you reach the last element.
<br>

## Implementation:
```python
class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


# Check if the tree is complete binary tree
def is_complete(root, index, numberNodes):

    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (is_complete(root.left, 2 * index + 1, numberNodes)
            and is_complete(root.right, 2 * index + 2, numberNodes))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
```
<br>

### Realtionship between array indexes and tree elements:
- Finding Child:
    - If index of any element is `i`:
        - left node: `2i+1`.
        - right node: `2i+2`.
- Findind Parent:
    - If index of any element id `i`:
        - parent: `lower_bound((i-1)/2)`
<br>

### Applications:
- Heap-based datastructure
- Heap sort

****************************************************************************
<br>
<br>
