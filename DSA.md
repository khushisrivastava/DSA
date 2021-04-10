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
- ## **Queue:**
