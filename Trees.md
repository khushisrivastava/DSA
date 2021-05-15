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

## **Balanced Binary Tree:**
Also refered as height-balanced Tree.<br>
Height of right and left sub tree of any node differ by not more than 1.

### Conditions:
- difference between left and right subtree is not more than 1.
- Both left and right subtree is balanced.
<br>

### Implementation:
```python
# CreateNode creation
class CreateNode:

    def __init__(self, item):
        self.item = item
        self.left = self.right = None


# Calculate height
class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0


# Check height balance
def is_height_balanced(root, CalculateHeight):

    left_height = CalculateHeight()
    right_height = CalculateHeight()

    if root is None:
        return True

    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)

    CalculateHeight.CalculateHeight = max(
        left_height.CalculateHeight, right_height.CalculateHeight) + 1

    if abs(left_height.CalculateHeight - right_height.CalculateHeight) <= 1:
        return l and r

    return False


CalculateHeight = CalculateHeight()

root = CreateNode(1)
root.left = CreateNode(2)
root.right = CreateNode(3)
root.left.left = CreateNode(4)
root.left.right = CreateNode(5)

if is_height_balanced(root, CalculateHeight):
    print('The tree is balanced')
else:
    print('The tree is not balanced')
```
<br>

### Applications:
- AVL Trees
- Balanced Binary Search Tree

****************************************************************************
<br>
<br>

## **Binary Search Tree:**
This allows us to maintain a sorted list of numbers.
- Binary Tree because maximum of 2 children per node.
- Search Tree because search number in `O(log(n))` time.

### Properties:
- All node of left subtree are less than root node.
- All node of right subtree are more than root node.
- Both subtrees of each node are also BST.
<br>

### Search Operation:
If the value is below the root, we can say for sure that the value is not in the right subtree; we need to only search in the left subtree and if the value is above the root, we can say for sure that the value is not in the left subtree; we need to only search in the right subtree.
- Algorithm:
    ```
    If root == NULL 
    return NULL;
    If number == root->data 
        return root->data;
    If number < root->data 
        return search(root->left)
    If number > root->data 
        return search(root->right)
- If value is found, we return that value so that it gets propogated in each recursive step.
- If value is not found, we reach left or right child of leaf node which is NULL and it gets propogated and returned.
<br>

### Insertion Operation:
Inserting a value in the correct position is similar to searching. We keep going to either right subtree or left subtree depending on the value and when we reach a point left or right subtree is null, we put the new node there.
- Algorithm:
    ```
    If node == NULL 
    return createNode(data)
    if (data < node->data)
        node->left  = insert(node->left, data);
    else if (data > node->data)
        node->right = insert(node->right, data);  
    return node
<br>

### Deletion Operation:
- CASE I:
    - In this case the node to be deleted is a leaf node, in such cases simply delete thee node from the tree.
- CASE II:
    - In this case the node to be deleted has one chlid node.
    1. Replace the node with its chlid node.
    2. Remove chlid node from original position.
- CASE III:
    - In this case the node to be deleted has 2 children.
    1. Get the inorder successor of the node.
    2. Replace the node with its successor.
    3. Remove successor from its original position.
<br>

### Implementation:
```python
# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
```
<br>

### Complexities:
- Time Complexity:
    Operation | Best Case | Average Case | Worst Case
    ----------|-----------|--------------|-----------
    Search | O(log(n)) | O(log(n)) | O(n)
    Insert | O(log(n)) | O(log(n)) | O(n)
    Delete | O(log(n)) | O(log(n)) | O(n)

- Space Complexity: O(n)
<br>

### Application:
- Multilevel indexing in database.
- Dynamic Storing.
- Managing virtual memory areas in UNIX kernel.

****************************************************************************
<br>
<br>

## **AVL Trees:**
- Self balancing BST
- Each node has an extra information called **balance factor**:
    - value can be -1, 0, +1
- Named after Georgy Adelson-Velsky and Landis.

### Balance Factor:
- Difference between height of left subtree and right subtree.
- The self balancing property  is maintained by the balance factor. Value should always be -1, 0 or +1.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/avl-tree-final-tree-1_0_2.png" height="40%" width="40%" >
<br>

### Rotating Subtree:
- **Left Rotation**: Arrangements of the nodes on right is transfered into the arrangements on left node.
    - Initial tree:<br>
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_leftrotate-1.png" height="20%" width="20%" >
    - If `y` has left subtree, assign `x` as parent of left subtree of `y`.
    - If parent of `x` is `NULL`, make `y` as root to the tree.
    - Else if `x` is left child of `p`, make `y` as left child of `p`; else make `y` as right child of `p`.
    - Make `y` as the parent of `x`.<br>
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_leftrotate-4.png" height="20%" width="20%" >

- **Right Rotation**: Arrangements of the nodes on left is transfered into the arrangements on the right node.
    - Initial tree:<br>
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_rightrotate-1.png" height="20%" width="20%" >
    - If `x` has right subtree, assign `y` as parent of right subtree of `x`.
    - If parent of `y` is `NULL`, make `x` as root of the tree.
    - Else if `y` is right child of `p`, make `x` as right child of `p`; else make `x` as left child of `p`.
    - Make `x` as parent of `y`.<br>
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/avl-tree_rightrotate-4.png" height="20%" width="20%" >

- **Left-Right Rotation**: Arrangement is first shifted to left and then right.
    - Do left rotation on `x-y`.<br>
        <img src="https://cdn.programiz.com/cdn/farfuture/-azcNvOPWv7wEnEzT3h227dYtZBlAL8CXtHdwXenr1c/mtime:1590639276/sites/tutorial2program/files/avl-tree-leftright-rotate-1.png" height="50%" width="50%" >
    - Do right rotation on `y-z`.<br>
        <img src="https://cdn.programiz.com/cdn/farfuture/gZrKUeMiHusFL-lb6gAaMCfK_edFDj64Qi3MwlYJ_jw/mtime:1590639281/sites/tutorial2program/files/avl-tree-leftright-rotate-2.png" height="50%" width="50%" >

- **Right-Left Rotation**: Arrangement is first shifted to right and then left.
    - Do right rotation on `x-y`.<br>
        <img src="https://cdn.programiz.com/cdn/farfuture/flq1MTO6SBcWdXIUda_BY4yhf9BLPRf7MT4Ip79vYF4/mtime:1590639294/sites/tutorial2program/files/avl-tree-rightleft-rotate-1.png" height="50%" width="50%" >
    - Do left rotation on `z-y`.<br>
        <img src="https://cdn.programiz.com/cdn/farfuture/MHtUIZ6EqUmgcC3exARGsdRiOFmENzCH-i_solZWi1g/mtime:1590639315/sites/tutorial2program/files/avl-tree-rightleft-rotate-2.png" height="50%" width="50%" >
<br>

### Insert a new node:
- Goto the appropriate root node.
    - If `newnode < rootnode`, call insertion algorithm on left subtree.
    - Elif `newnode > rootnode`, call intertion algorithm on right subtree.
    - Else return `leafnode`.
- Compare `leafnode` with `newnode`.
    - If `newnode < leafnode`, make `newnode` left child of `leafnode`.
    - Else make `newnode` right child of `leafnode`.
- Update `Balance Factor` of the nodes.
- If nodes are unbalanced, then rebalance the tree.
    - If `balance factor > 1` => height of left subtree is greater than right subtree.
        - If `newnode < leafnode`, do right rotation.
        - Else do left rotation.
    - If `balance factor < -1` => height of right subtree is greater than left subtree.
        - If `newnode > leafnode`, do left rotation.
        - ELse do right rotation.
<br>

### Delete a node:
- Locate the node `tobedeleted`.
- 3 cases:
    - If `tobedeleted` is a leaf node, remove the node.
    - Elif `tobedeleted` has 1 child, subsitute content of `tobedeleted` with child node and remove the child.
    - Elif `tobedeleted` had 2 children, find inorder successor of `tobedeleted` and substitude their contents and remove the successor.
- Update `balance factor` of the nodes.
- Rebalance the tree.
    - If `balance factor > 1` of `currentnode`
        - If `balance factor` of `leftchild >= 0`, do right rotation.
        - Else do left rotation.
    - If `balance factor < -1` of `currentnode`
        - If `balance factor` of `rightchild <= 0`, do left rotation.
        - Else do right rotation.
<br>

### Implementation:
```python
import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)
```
<br>

### Complexities:
Insert | Delete | Search
-------|--------|-------
O(log(n)) | O(log(n)) | O(log(n))
<br>

### Application:
- Indexing large records in database.
- Searching in large database.

****************************************************************************
<br>
<br>
