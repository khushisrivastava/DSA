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
<!-- - ## Circular Queue -->
