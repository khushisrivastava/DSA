# DSA LEARNING
<br>

- ## **Asymtotic Notations**:
    - ### *Big O Notation* -
        - o(n)
        - Represents Upper bond.
        - Gives Worst-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/big0.png" height="50%" width="50%" >

    - ### *Omega Notation* - 
        - Ω(n)
        - Represents Lower bond.
        - Gives Best-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/omega.png" height="50%" width="50%" >

    - ### *Theta Notation* - 
        - Θ(n)
        - Encloses the function from above and below.
        - Gives Average-Case complexity.

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/theta.png" height="50%" width="50%" >


    ****************************************************
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

    ******************************************************
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

    <img src="https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png" height="70%" width="70%" >
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

    ****************************************************************************
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
        
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/Queue-program-enqueue-dequeue.png" height="70%" width="70%" >
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

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/simple-queue_0.png" height="70%" width="70%" >
    - Circular Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-queue.png" height="70%" width="70%" >
    - Priority Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/priority-queue.png" height="70%" width="70%" >
    - Double Ended Queue

        <img src="https://cdn.programiz.com/sites/tutorial2program/files/double-ended-queue.png" height="70%" width="70%" >
    
    *****************************************************************************
    <br>
    <br>

- ## Circular Queue:
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
        <img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-queue-program.png" height="70%" width="70%" >
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

- ## Priority Queue:
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
