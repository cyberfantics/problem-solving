# Day 1: Introduction to Data Structures and Complexity Analysis

## What are Data Structures?

A **data structure** is a way of organizing and storing data so that it can be accessed and modified efficiently. They define:
- **Data Values**: The information you're dealing with.
- **Relationships**: How these values are connected.
- **Operations**: Functions or operations that can be applied to the data.

### Common Examples of Data Structures:

1. **Arrays**:
   - A collection of elements, each identified by an index.
   - Example: `int arr[5] = {1, 2, 3, 4, 5};`
   - Accessing an element: `arr[2]` gives `3` (constant time: O(1)).    
    - Learn more about common array operations and their time and space complexities [here](./Array.md).

2. **Linked Lists**:
   - A linear collection of elements, where each element points to the next.
   - Example: `1 -> 2 -> 3 -> 4 -> 5`
   - Insertions and deletions can be done efficiently, but accessing elements is slower (linear time: O(n)).

3. **Stacks**:
   - Follows **LIFO** (Last In First Out) principle. Think of a stack of plates.
   - Example: `push(5) -> push(3) -> pop() -> result: 3`
   - Used in algorithms like recursion, DFS (Depth-First Search).

4. **Queues**:
   - Follows **FIFO** (First In First Out) principle.
   - Example: `enqueue(5) -> enqueue(3) -> dequeue() -> result: 5`
   - Used in BFS (Breadth-First Search), and scheduling algorithms.

5. **Trees**:
   - A hierarchical structure consisting of nodes, each node has a value and references to child nodes.
   - Example: Binary Tree with root `10` and children `5` and `20`.
     ```
         10
        /  \
       5    20
     ```
   - Trees are used in searching (BSTs), representing hierarchical data (file systems), etc.

6. **Hash Tables**:
   - Store key-value pairs and provide fast lookups.
   - Example: `{ "apple": 1, "banana": 2, "cherry": 3 }`
   - Lookup time: O(1) if no collisions occur.

---

## Why Learn Data Structures for Coding Interviews?

In coding interviews, you are given input data and asked to write an algorithm to manipulate it to achieve the desired output. Here's why data structures are critical:

1. **Input and Output are Just Data**: How efficiently you store and manipulate this data can determine your solution’s speed.
   
2. **Multiple Solutions Exist**: 
   - Example: For finding duplicates in an array, you could:
     - Use nested loops (O(n^2)), or
     - Use a hash set (O(n)) for a more optimal solution.

3. **Efficiency Matters**: 
   - Knowing when to use a particular data structure can dramatically improve performance.
   - Example: Using a heap to find the kth largest element in an array is more efficient than sorting the entire array.

---

## Complexity Analysis: Time and Space

### Why Do We Need Complexity Analysis?

To evaluate the efficiency of an algorithm, we need to measure:
- **Time Complexity**: How does the execution time increase with input size?
- **Space Complexity**: How much memory does the algorithm use as the input grows?

### What is Time Complexity?

Time complexity tells us how the runtime of an algorithm changes as the input size grows. We express it in **Big O Notation**.

#### Examples:
- **O(1)**: Constant time. The operation takes the same time regardless of input size.
  - Example: Accessing an array element by index `arr[i]`.

- **O(n)**: Linear time. The operation scales linearly with the size of the input.
  - Example: Iterating over an array of size `n`.

- **O(log n)**: Logarithmic time. Typically occurs when the problem size is halved at each step.
  - Example: Binary Search on a sorted array.

### Big O Notation: Upper Bound of Complexity

Big O describes the worst-case scenario for how long an algorithm will take. For example:
- **O(n^2)**: Nested loops where each loop runs `n` times.
  - Example: Comparing every pair of elements in an array (Bubble Sort).

### Common Time Complexities and Their Examples:
1. **O(1)** – Constant Time: Accessing an element in an array.
2. **O(n)** – Linear Time: Traversing an entire list.
3. **O(log n)** – Logarithmic Time: Binary Search in a sorted array.
4. **O(n log n)** – Linearithmic Time: Merge Sort, Heap Sort.
5. **O(n^2)** – Quadratic Time: Bubble Sort, Selection Sort.
6. **O(2^n)** – Exponential Time: Solving the Tower of Hanoi, brute-force combinations.

---

## Space Complexity

Space complexity measures how much additional memory an algorithm uses as the input grows. 

#### Example:
- **O(1)**: Algorithm uses constant memory, regardless of input size.
  - Example: Swapping two numbers.
  
- **O(n)**: Algorithm uses additional memory proportional to the input size.
  - Example: Storing elements in a new array.

---

## Techniques to Simplify Big O Expressions

1. **Drop constants**:
   - `O(2n)` is simplified to `O(n)` because constants don't affect growth rates.
   
2. **Focus on the dominant term**:
   - `O(n^2 + n)` simplifies to `O(n^2)` because the dominant term is the one that grows the fastest.

---

## Logarithms

Logarithms often appear in algorithms where the data set is halved repeatedly (such as binary search). 

- **Example**: Binary search works on a sorted array. With every comparison, we reduce the problem size by half.
  - Input: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
  - To find `6`, start at the midpoint (`5`). Then eliminate half of the data after each comparison.
  - Time complexity: **O(log n)**.

---