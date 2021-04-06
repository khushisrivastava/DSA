# DSA LEARNING
<br>

- ## **Asymtotic Notations**:
    - ### *Big O Notation* -
        - o(n)
        - Represents Upper bond.
        - Gives Worst-Case complexity.
        ![Big O](https://cdn.programiz.com/sites/tutorial2program/files/big0.png)

    - ### *Omega Notation* - 
        - Ω(n)
        - Represents Lower bond.
        - Gives Best-Case complexity.
        ![Omega](https://cdn.programiz.com/sites/tutorial2program/files/omega.png)

    - ### *Theta Notation* - 
        - Θ(n)
        - Encloses the function from above and below.
        - Gives Average-Case complexity.
        ![Theta](https://cdn.programiz.com/sites/tutorial2program/files/theta.png)


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
