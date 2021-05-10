# <center> DSA LEARNING
<br>

- ## **Asymtotic Notations**:
    - ### *Big O Notation* -
        - o(n)
        - Represents Upper bond.
        - Gives Worst-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/big0.png" height="30%" width="30%" >

    - ### *Omega Notation* - 
        - Ω(n)
        - Represents Lower bond.
        - Gives Best-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/omega.png" height="30%" width="30%" >

    - ### *Theta Notation* - 
        - Θ(n)
        - Encloses the function from above and below.
        - Gives Average-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/theta.png" height="30%" width="30%" >


    *************************************************************************************************
<br>
<br>

- ## **Divide and Conqure Algorithm:**
    ### Concept:
    - **Divide** - Divide the problems into subproblems using recursion.
    - **Conquer** - Solve smaller sub-problems *(recursively)*.
    - **Combine** - Combine the result of sub-problems to solve the actual problem.
    <br>
    
    ### Time Complexity: O(nlog(n))
    <br>

    ### Divide and Conquer v/s Dynamic Approach:
    Divide and Conquer | Dynamic Approach
    -------------------|-----------------
    Result of subproblems not stored for future reference | Results are stored for future reference
    Use when sub problem is not solved multiple times | Use when result of subproblem is to be used
    <br>
    
    ### Applications:
    - Binary Search
    - Merge Sort
    - Quick Sort
    - Strassen's Matrix multiplication
    - Karatsuba Algorithm

    **********************************************************************************************
<br>
<br>

- ## **Stack:**
    ### Concept:
    - Like pile of notebooks - 
        - put on top
        - remove from top
    - **Abstract Data Type**
    - **LIFO** principle - Last In First Out
        - push - putting an element on top of stack
        - pop - removing an element

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/stack.png" height="50%" width="50%" >
        <br>
    
    ### Operations:
    - **Push** - Add element on top of stack.
    - **Pop** - Remove element from top of stack.
    - **IsEmpty** - Check if stack is empty.
    - **IsFull** - Check if stack is full.
    - **Peek** - Get value of top element without removing it.
    <br>

    ### Working:
    1. `TOP` is used to keep track of top element in stack.
    2. While initializing: `TOP = -1`. Can check if stack is empty by condition `TOP == -1` .
    3. On pushing: `TOP` is increased by 1 and new element is placed at the position of `TOP`.
    4. On popping: return the value of element at `TOP` and reduce its value by 1.
    5. Before pushing: check if stack is full.
    6. Before popping: check if stack is empty.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png" height="50%" width="50" >
    <br>

    ### Implementation:
    ```python
    # Creating a stack
    def create_stack():
        stack = []
        return stack


    # Creating an empty stack
    def check_empty(stack):
        return len(stack) == 0


    # Adding items into the stack
    def push(stack, item):
        stack.append(item)
        print("pushed item: " + item)


    # Removing an element from the stack
    def pop(stack):
        if (check_empty(stack)):
            return "stack is empty"

        return stack.pop()


    stack = create_stack()
    push(stack, str(1))
    push(stack, str(2))
    push(stack, str(3))
    push(stack, str(4))
    print("popped item: " + pop(stack))
    print("stack after popping an element: " + str(stack))
    ```
    <br>

    ### Time Complexity: O(1)
    <br>

    ### Application: 
    - **Reverse a word or string**
    - **Calculate prefix or postfix value**
    - **Browser back button**

    *************************************************************************************
<br>
<br>

- ## **Queue / Simple Queue:**
    ### Concept:
    - Ticket Queue:
        - Enters first
        - Gets tickect first
    - **FIFO Rule** - First In First Out
    - Enqueque - Putting in the item in the list
    - Dequeue -  Removing the item form list 
    <br>

    ### Operations:
    - **Enqueue** - Add element to the end of queue.
    - **Dequeue** - Remove an element from the front of queue.
    - **IsEmpty** - Check if queue is empty.
    - **IsFull** - Check if queue is full.
    - **Peek** - Get value of first element without removing it.
    <br>

    ### Working:
    - 2 pointers - `FRONT` to track first element and `REAR` to track last element.
    - Initially both `FRONT` and `REAR` set to `-1`.
    - **Enqueue** - 
        - Check if queue is full.
        - For 1st element, set value of `FRONT` and `REAR` to `0`.
        - For adding a new element, increase `REAR` by `1` and insert element in the position pointed by it.
    - **Dequeue** - 
        - Check if queue is empty.
        - Return the value pointed by `Front` and increase its value by `1`.
        - For the last element, i.e when `FRONT == REAR`, reset the value of both to `-1`.
        
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/Queue-program-enqueue-dequeue.png" height="40%" width="40%" >
    <br>

    ### Implementtation:
    ```python
    class Queue:

        def __init__(self):
            self.queue = []

        # Add an element
        def enqueue(self, item):
            self.queue.append(item)

        # Remove an element
        def dequeue(self):
            if len(self.queue) < 1:
                return None
            return self.queue.pop(0)

        # Display  the queue
        def display(self):
            print(self.queue)

        def size(self):
            return len(self.queue)


    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    q.display()

    q.dequeue()

    print("After removing an element")
    q.display()
    ```
    <br>

    ### Limitation:
    After few enqueue and dequeue operation the size of queue reduces. We can only use the indexes smaller than `FRONT` only when both `FRONT` and `REAR` is set to initial.<br>
    To solve this: ***Circular Queue***
    <br>

    ### Time Complexity: O(1)
    <br>

    ### Applications:
    - CPU and Disk Scheduling
    - Queue is used to synchronise asynchronous data transfer.
    - Handeling interrupt in real-time system.
    - Call center phone system - to hold people calling them in order.
    <br>

    ### Types:
    - Simple Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/simple-queue_0.png" height="50%" width="50%" >
    - Circular Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-queue.png" height="50%" width="50%" >
    - Priority Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/priority-queue.png" height="50%" width="50%" >
    - Double Ended Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/double-ended-queue.png" height="50%" width="50%" >
    

    *************************************************************************************
<br>
<br>

- ## **Circular Queue:**
    ### Working -
    - Circular Increment
    - When `REAR` reaches the end of the queue, we start by beigning of the queue.
    - Performed by modulo division with size of queue.
    - `if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)`        
    <br>

    ### Operations:
    - 2 pointers - `FRONT` to track first element and `REAR` to track last element.
    - Initially both `FRONT` and `REAR` set to `-1`.
    - **Enqueue** -
        - Check if queue is full.
        - For 1st element, set value of `FRONT` and `REAR` to `0`.
        - For adding a new element, circularly increase `REAR` by `1` (if reaches the end, next it would be at the start of the queue) and insert element in the position pointed by it.
    - **Dequeue** - 
        - Check if queue is empty.
        - Return the value pointed by `Front` and circularly increase its value by `1`.
        - For the last element, i.e when `FRONT == REAR`, reset the value of both to `-1`.
    - **IsFull** - 2 cases:
        - ```
            FRONT == 0 and REAR == SIZE -1 or FRONT == REAR + 1 
            ```
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-queue-program.png" height="40%" width="40%" >
    <br>

    ### Implementation:
    ```python
    class MyCircularQueue():

        def __init__(self, k):
            self.k = k
            self.queue = [None] * k
            self.head = self.tail = -1

        # Insert an element into the circular queue
        def enqueue(self, data):

            if ((self.tail + 1) % self.k == self.head):
                print("The circular queue is full\n")

            elif (self.head == -1):
                self.head = 0
                self.tail = 0
                self.queue[self.tail] = data
            else:
                self.tail = (self.tail + 1) % self.k
                self.queue[self.tail] = data

        # Delete an element from the circular queue
        def dequeue(self):
            if (self.head == -1):
                print("The circular queue is empty\n")

            elif (self.head == self.tail):
                temp = self.queue[self.head]
                self.head = -1
                self.tail = -1
                return temp
            else:
                temp = self.queue[self.head]
                self.head = (self.head + 1) % self.k
                return temp

        def printCQueue(self):
            if(self.head == -1):
                print("No element in the circular queue")

            elif (self.tail >= self.head):
                for i in range(self.head, self.tail + 1):
                    print(self.queue[i], end=" ")
                print()
            else:
                for i in range(self.head, self.k):
                    print(self.queue[i], end=" ")
                for i in range(0, self.tail + 1):
                    print(self.queue[i], end=" ")
                print()


    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(5)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.enqueue(4)
    obj.enqueue(5)
    print("Initial queue")
    obj.printCQueue()

    obj.dequeue()
    print("After removing an element from the queue")
    obj.printCQueue()
    ```            
    <br>

    ### Time Complexity: O(1)
    <br>

    ### Applications:
    - CPU Scheduling
    - Memory Management
    - Traffic Management
    
    **************************************************************************************
<br>
<br>

- ## **Priority Queue:**
    ### Understanding: 
    - Each element is associated with a priority and is served according to that.
    - If elements have same priority then served according to order in queue.
    <br>

    ### Implementation: 
    - Implemented using -
        - Array
        - Linked List
        - Heap (Most Efficient)
        - BST
    - Time Complexity -  

        Operations | peek | insert | delete
        ---------- | ---- | ------ | ------
        Linked List | O(1) | O(n) | O(1)
        Binary Heap | O(1) | O(log n) | O(log n)
        Binary Search Tree | O(1) | O(log n) | O(log n)
    <br>

    ### Operations:
    - Insert -
        1. Insert element to the end of the tree.
        2. Heapify the tree.
        - ```
            if there is no node, 
            create a newNode.
            else (if a node is already present)
            insert the newNode at the end (last node from left to right.)
            
            heapify the array
            ```
    - Delete - 
        1. Select the elemenet to be deleted and swap with the last element.
        2. Remove the last element.
        3. Heapify the tree.
        - ```
            If nodeToBeDeleted is the leafNode
            remove the node
            Else swap nodeToBeDeleted with the lastLeafNode
            remove noteToBeDeleted
            
            heapify the array
            ```
    - Peek -
        - Return max element from max-heap and min element from min-heap
        - `return rootNode`
    <br>

    ### Implementation:
    ```python
    # Function to heapify the tree
    def heapify(arr, n, i):
        # Find the largest among root, left child and right child
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        # Swap and continue heapifying if root is not largest
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)


    # Function to insert an element into the tree
    def insert(array, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum)
            for i in range((size // 2) - 1, -1, -1):
                heapify(array, size, i)


    # Function to delete an element from the tree
    def deleteNode(array, num):
        size = len(array)
        i = 0
        for i in range(0, size):
            if num == array[i]:
                break

        array[i], array[size - 1] = array[size - 1], array[i]

        array.remove(size - 1)

        for i in range((len(array) // 2) - 1, -1, -1):
            heapify(array, len(array), i)


    arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print ("Max-Heap array: " + str(arr))

    deleteNode(arr, 4)
    print("After deleting an element: " + str(arr))
    ```
    <br>

    ### Application:
    - Dijkstra's algorithm
    - Implementing stack
    - Load balancing and interrupt handeling in os.
    - Data compression in Huffman code.
    
    ******************************************************************************************
<br>
<br>

- ## **Deque:**
    ### Concept:
    - Insertion and Removal can be perfromed from both the ends.
    - Do not follow **FIFO**.
    - TYPES:
        - **Input Restricted Deque**:
        Input restricted from single end but output from both the ends.
        - **Output Restricted Deque**:
        Output restricted from single end but input from both the ends.
    <br>

    ### Operations:
    - An array of size `n` and 2 pointers `FRONT = -1` and `REAR = 0`.
    - **Insert at front** -
        - If `FRONT < 1`. Set `FRONT = n - 1` else `FRONT -= 1`.
        - Insert element at the position of `FRONT`.
    - **Insert at rear** -
        - If array if full `REAR = 0`. 
        - Else `REAR += 1`.
        - Insert element at the position of `REAR`.
    - **Delete from from** - 
        - Check if array is empty.
        - If `FRONT == REAR`, set `FRONT = REAR = -1`.
        - Else if `FRONT == n - 1`, set `FRONT = 0`.
        - Else set `FRONT += 1`.
    - **Delete from rear** -
        - Check if array is empty.
        - If `FRONT == REAR`, set `FRONT = REAR = -1`.
        - Else if `REAR == 0`, set `REAR = n - 1`.
        - Else `REAR -= 1`.
    - **Check empty** - `FRONT == -1`
    - **Check full** - `FRONT == 0` and `REAR == n - 1` or `FRONT == REAR + 1`.
    <br>

    ### Implementation:
    ```python
    class Deque:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def addRear(self, item):
            self.items.append(item)

        def addFront(self, item):
            self.items.insert(0, item)

        def removeFront(self):
            return self.items.pop(0)

        def removeRear(self):
            return self.items.pop()

        def size(self):
            return len(self.items)


    d = Deque()
    print(d.isEmpty())
    d.addRear(8)
    d.addRear(5)
    d.addFront(7)
    d.addFront(10)
    print(d.size())
    print(d.isEmpty())
    d.addRear(11)
    print(d.removeRear())
    print(d.removeFront())
    d.addFront(55)
    d.addRear(45)
    print(d.items)
    ```
    <br>

    ### Time Complexity: O(1)
    <br>

    ### Applications:
    - Undo Software operations
    - Store browser history
    - Implementiong stacks and queue
    
    **************************************************************************************
<br>
<br>

- ## **Linked List:**
    ### Understanding:
    - Series of connected nodes. Each node stores data and address of next node.
    - Address of first node is given as `HEAD`.
    - Address to next node is `NULL` in the last node.
    - Ability to break the chain and rejoin it.
    <br>

    ### Implementation:
    ```python
    class Node:
        # Creating a node
        def __init__(self, item):
            self.item = item
            self.next = None


    class LinkedList:

        def __init__(self):
            self.head = None


    if __name__ == '__main__':

        linked_list = LinkedList()

        # Assign item values
        linked_list.head = Node(1)
        second = Node(2)
        third = Node(3)

        # Connect nodes
        linked_list.head.next = second
        second.next = third

        # Print the linked list item
        while linked_list.head != None:
            print(linked_list.head.item, end=" ")
            linked_list.head = linked_list.head.next
    ```
    <br>

    ### Complexity:
    - Time:
        - *Search* - O(n)
        - *Insert* - O(1)
        - *Delete* - O(1)
    - Space - O(n)
    <br>

    ### Application:
    - Dynamic memory allocation.
    - Implemented in stack and queue.
    - UNDO functionalities.
    - Hash tables, Graphs.
    <br>

    ### Operations:
    - **Traverse**
        - Displaying the content of list.
        - Keep moving the `temp` node to the next node and display its content. If `temp` is `NULL` => we have reached the end of the list.
    
    - **Insert**
        - Adding elements to list.
        - *Insert at the beigning*:
            1. Allocate memory for new node and store data.
            2. `new_node.next = head`.
            3. `head = new_node`.
        - *Insert at the end*:
            1. Allocate memory for new node and store data.
            2. Traverse to last node.
            3. `temp.next = new_node`.
        - *Insert at the middle*:
            1. Allocate memory for new node and store data. 
            2. Traverse to the node just before the required position of the `new_node`.
            3. `new_node.next = temp.next`.
            4. `temp.next = new_node`.
    
    - **Delete**
        - Deleting node from the list.
        - *Delete from beigning*:
            1. `head = head.next`.
        - *Delete from end*:
            1. Traverse to second last element.
            2. `temp.next = NULL`.
        - *Delete from middle*:
            1. Traverse to the element before the element to be deleted.
            2. `temp.next = temp.next.next`.
    <br>

    ### Implementation of Operations:
    ```python
    # Create a node
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None


    class LinkedList:

        def __init__(self):
            self.head = None

        # Insert at the beginning
        def insertAtBeginning(self, data):
            new_node = Node(data)

            new_node.next = self.head
            self.head = new_node

        # Insert after a node
        def insertAfter(self, node, data):

            if node is None:
                print("The given previous node must inLinkedList.")
                return

            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

        # Insert at the end
        def insertAtEnd(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            last = self.head
            while (last.next):
                last = last.next

            last.next = new_node

        # Deleting a node
        def deleteNode(self, position):

            if self.head == None:
                return

            temp_node = self.head

            if position == 0:
                self.head = temp_node.next
                temp_node = None
                return

            # Find the key to be deleted
            for i in range(position - 1):
                temp_node = temp_node.next
                if temp_node is None:
                    break

            # If the key is not present
            if temp_node is None:
                return

            if temp_node.next is None:
                return

            next = temp_node.next.next
            temp_node.next = None
            temp_node.next = next

        def printList(self):
            temp_node = self.head
            while (temp_node):
                print(str(temp_node.item) + " ", end="")
                temp_node = temp_node.next


    if __name__ == '__main__':

        llist = LinkedList()
        llist.insertAtEnd(1)
        llist.insertAtBeginning(2)
        llist.insertAtBeginning(3)
        llist.insertAtEnd(4)
        llist.insertAfter(llist.head.next, 5)

        print('Linked list:')
        llist.printList()

        print("\nAfter deleting an element:")
        llist.deleteNode(3)
        llist.printList()
    ```
    <br>

    ### Types:
    - **Singly linked list**:
        <br>Each node has data and a pointer to the next node.
        
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/linked-list-concept_0.png" height="50%" width="50%" >
    
    - **Doubly linked list**:
        <br>A pointer to previous node so tranverse in both forward and backward direction.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/doubly-linked-list-concept.png" height="50%" width="50%" >
    
    - **Circular linked list**:
        <br>Last node is linked to first node forming a circular loop.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-linked-list.png" height="50%" width="50%" >
    
    ****************************************************************************************
<br>
<br>

- ## **Hash Tables:**
    ### Concept:
    Stores element in key valur pair.
    - ***Key*** : Unique. Used for indexing values.
    - ***Value*** : Data to be stored.
    <br>

    ### Hashing (Hash Fuction):
    In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.
    - `k` is key `h(x)` is hash function.
    - `h(x)` gives index to store element in key.

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/Hash-2_0.png" height="60%" width="60%" >

    - It is a processing of mapping large arbitrary data to tabular indexes.
    - **Time Complexity: O(1).**
    - 
    <br>

    ### Hash Collision:
    - When hash function generates same indexfor multiple keys.
    - Resolved using 2 techniques:
        - Collision resolution by chaining.
        - Open Addressing (Liner/Quadratic Probing and Double Hashing)
    <br>

    - ### **Collision Resolution by chaining:**
        - Elements are stored in same the same index, using a doubly linked list.
        - if `j` is the index, it stores address of the head of the list of items. If list is empty `j = NULL`.
        - Pseudocode:
        ```
        chainedHashSearch(T, k)
        return T[h(k)]
        chainedHashInsert(T, x)
        T[h(x.key)] = x //insert at the head
        chainedHashDelete(T, x)
        T[h(x.key)] = NIL
        ```

    - ### **Open Addressing:**
        - Does not store multiple element in same index.
        - Index is either filled with a single key or left `NULL`.
        - **Liner Probing**:
            - Collision resolved by checking next slot.
            - `h(k, i) = (h′(k) + i) mod m`<br>
                i = 1,2,3,....<br>
                h'(k) = new hash funtion
            - If collision at h(k,0) -> h(k,1) is checked.<br>
                Value of `i` is linearly incremented.
            - Time Complexity - O(n)
        - **Quadratic Probing**:
            - Similar to liner probing but next slot is given by:<br>
                `h(k,i) = (h'(k) + c1i1 + c2i2) mod m`<br>
                c1, c2 = constants<br>
                i = 1,2,3....
        - **Double Hashing**:
            - If collision occures after h(k), another hash function is used for geting next free slot.
            - `h(k, i) = (h1(k) + ih2(k)) mod m`
    <br>

    ### Good Hash Function:
    - Reduces number of collisions.
    1. **Division Method:**
        - If `k` is key and `m` is size of hash table, <br>
            `h(k) = k mod m`
    2. **Multiplication Method:**
        - `h(k) = ⌊m(kA mod 1)⌋`<br>
            `kA mod 1` gives the fractional part `kA`<br>
            `⌊ ⌋` gives the floor value<br>
            `A` is constant between 0 and 1. Optimally `(√5-1)/2` (Knuth suggestion)
    3. **Universal Hashing:**
        - Hash function is chosen at random independent of keys.
    <br>

    ### Implementation:
    ```python
    hashTable = [[],] * 10

    def checkPrime(n):
        if n == 1 or n == 0:
            return 0

        for i in range(2, n//2):
            if n % i == 0:
                return 0

        return 1


    def getPrime(n):
        if n % 2 == 0:
            n = n + 1

        while not checkPrime(n):
            n += 2

        return n


    def hashFunction(key):
        capacity = getPrime(10)
        return key % capacity


    def insertData(key, data):
        index = hashFunction(key)
        hashTable[index] = [key, data]

    def removeData(key):
        index = hashFunction(key)
        hashTable[index] = 0

    insertData(123, "apple")
    insertData(432, "mango")
    insertData(213, "banana")
    insertData(654, "guava")

    print(hashTable)

    removeData(123)

    print(hashTable)
    ```
    <br>

    ### Applications:
    - For constant time lookup and insertion
    - Cryptographic applications
    - Data indexing

    *****************************************************************************************
<br>
<br>

- ## **Heap DataStructure:**
    ### Concept:
    - Data structure that satisfies heap property and is a complete binary tree.
    - Complete Binary Tree:
        - Every level except the late is completely filled.
        - Nodes are as far as possible
    - Heap Property:
        - ***Max Heap***: Key of each node is greater than its child node. Root node is the largest.
        - ***Min Heap***: Key of eash node is smaller than its child node. Root node is the smallest.
    <br>

    ### Operation:
    - **Heapify**:
        1. Create a complete binary tree of the array.
        2. Set `i` as 1st index of non-leaf node, given by `n/2 - 1`.
        3. Set `i = largest`.
        4. If leftChild(`2i+1`) is greater than `i`, set `leftChildIndex = largest`.<br>
        If rightChlid(`2i+2`) is greater than `largest`, set `rightChildIndex = largest`.
        5. Swap `largest` with `i`.
        6. Repeat step 3-5.
    - **Insert**:
        1. Insert new element at the end.
        2. Heapify.
    - **Delete**:
        1. Swap the required node with last element.
        2. Remove the last element.
        3. Heapify.
    - **Peek**:
        1. return `RootNode`.
    <br>

    ### Implementation:
    ```python
    # Max-Heap data structure in Python

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2 
        
        if l < n and arr[i] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            heapify(arr, n, largest)

    def insert(array, newNum):
        size = len(array)
        if size == 0:
            array.append(newNum)
        else:
            array.append(newNum);
            for i in range((size//2)-1, -1, -1):
                heapify(array, size, i)

    def deleteNode(array, num):
        size = len(array)
        i = 0
        for i in range(0, size):
            if num == array[i]:
                break
            
        array[i], array[size-1] = array[size-1], array[i]

        array.remove(num)
        
        for i in range((len(array)//2)-1, -1, -1):
            heapify(array, len(array), i)
        
    arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print ("Max-Heap array: " + str(arr))

    deleteNode(arr, 4)
    print("After deleting an element: " + str(arr))
    ```
    <br>

    ### Application:
    - Implementing Priority Queue.
    - Dijkstra’s Algorithm
    - Heap Sort
    
    *****************************************************************************************
<br>
<br>
