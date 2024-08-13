from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Helper function for backtracking
        def backtrack(start, path, remaining_target):
            # If the remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(path[:])  # Add a copy of the current path to the result
                return
            
            # If the remaining target is negative, stop exploring further
            if remaining_target < 0:
                return
            
            # Iterate over the candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                # Skip duplicates by checking if the current candidate is the same as the previous one
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Add the current candidate to the path
                path.append(candidates[i])
                
                # Recursively explore further with updated remaining target and next start index
                backtrack(i + 1, path, remaining_target - candidates[i])
                
                # Remove the last element to backtrack and explore other combinations
                path.pop()

        # Sort the candidates to easily manage duplicates
        candidates.sort()
        
        result = []  # List to store all unique combinations
        backtrack(0, [], target)  # Start backtracking from index 0 with an empty path and full target
        return result  # Return the list of unique combinations


'''
Why we Use typing library

The `typing` library in Python is used to provide type hints, which help indicate the expected data types of variables, function parameters, and return values. Type hints make the code more readable, easier to understand, and can catch errors earlier in the development process by providing information about the expected types.

### Key Reasons to Use the `typing` Library:

1. Improved Code Clarity: 
   - By specifying the types of inputs and outputs, other developers (or your future self) can more easily understand what kind of data the function expects and returns.
   - Example:
     ```python
     def add(a: int, b: int) -> int:
         return a + b
     ```
     Here, it's clear that `a` and `b` should be integers, and the function will return an integer.

2. Early Error Detection:
   - Type hints can help identify potential bugs or issues during development. Tools like linters (e.g., `mypy`) can check your code for type consistency before you run it.
   - Example:
     ```python
     def greet(name: str) -> str:
         return "Hello, " + name
     
     greet(123)  # This would raise a type-checking warning.
     ```

3. Enhanced IDE Support:
   - Many Integrated Development Environments (IDEs) and text editors use type hints to provide better autocomplete suggestions, inline type checking, and more intelligent code navigation.
   
4. Documentation:
   - Type hints act as a form of documentation. When you specify types, you're also documenting your code, making it easier for others to understand how to use your functions and classes.

### Example in the Context of the Problem:
In the "Combination Sum II" solution, the `typing` library is used to specify that the `candidates` parameter is a list of integers (`List[int]`), and the return value is a list of lists of integers (`List[List[int]]`).

'''