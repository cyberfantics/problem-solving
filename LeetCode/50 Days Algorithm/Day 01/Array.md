# Big O of Common Array Operations (Time and Space Complexity)

## How Arrays are Stored in Memory

Arrays are stored in **contiguous blocks of memory**. This means that each element in the array is located right next to the previous one, with no gaps between them. The main advantages of this layout are:

- **Direct access to elements**: Because each element is placed next to the previous one, the memory address of any element can be computed directly using the array’s base address and the index.
- **Constant time access**: You can access any element in an array in constant time `O(1)` because the memory address is calculated as:

---

## 1. Accessing an Element
- **Time Complexity**: `O(1)` (Constant Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Accessing an element in an array requires constant time and space since no additional memory is used.
- **Example**: Accessing `arr[2]` in `arr = [5, 10, 15, 20]` takes constant time and space.

## 2. Setting an Element
- **Time Complexity**: `O(1)` (Constant Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Setting an element involves updating the existing space, not allocating new space.
- **Example**: `arr[1] = 12` updates an element without using extra memory.

## 3. Traverse/Search
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Traversing or searching through an array takes linear time, but requires no additional space beyond storing the array itself.
- **Example**: To find an element, we scan each element one by one.

## 4. Copying an Array
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(n)` (Linear Space)
- **Explanation**: Copying requires time proportional to the number of elements, and new memory equal to the size of the array is allocated.
- **Example**: Copying `arr = [1, 2, 3]` to another array takes `O(n)` time and space.

## 5. Insertion
### Inserting at the Beginning
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Inserting at the beginning requires shifting all elements to the right, but no additional space is needed except for the new element.
- **Example**: Inserting `0` at the start of `arr = [1, 2, 3]`.

### Inserting at the End
- **Time Complexity**: `O(1)` (Constant Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Inserting at the end doesn't require shifting, and no extra space is needed except for the new element.
- **Example**: Appending `4` to `arr = [1, 2, 3]`.

### Inserting Somewhere in Between
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Inserting an element in the middle requires shifting all subsequent elements, but no additional memory is required except for the new element.
- **Example**: Inserting `10` at index `2` in `arr = [1, 2, 3, 4]`.

## 6. Removal
### Removing from the Beginning
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Removing from the beginning requires shifting all subsequent elements to the left, but no new space is required.
- **Example**: Removing `1` from `arr = [1, 2, 3]` requires shifting elements.

### Removing from the End
- **Time Complexity**: `O(1)` (Constant Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Removing the last element is a constant-time operation and requires no additional memory.
- **Example**: Removing `3` from `arr = [1, 2, 3]` takes constant time and space.

### Removing Somewhere in Between
- **Time Complexity**: `O(n)` (Linear Time)
- **Space Complexity**: `O(1)` (Constant Space)
- **Explanation**: Removing an element from the middle requires shifting subsequent elements, but no extra memory is needed.
- **Example**: Removing `2` from `arr = [1, 2, 3, 4]`.

---

### Summary Table of Time and Space Complexity for Array Operations

| Operation                | Time Complexity | Space Complexity |
|--------------------------|-----------------|------------------|
| Access                   | O(1)            | O(1)             |
| Set                      | O(1)            | O(1)             |
| Traverse/Search          | O(n)            | O(1)             |
| Copy                     | O(n)            | O(n)             |
| Insert at Beginning       | O(n)            | O(1)             |
| Insert at End             | O(1)            | O(1)             |
| Insert Somewhere in Between | O(n)            | O(1)             |
| Remove at Beginning       | O(n)            | O(1)             |
| Remove at End             | O(1)            | O(1)             |
| Remove Somewhere in Between | O(n)            | O(1)             |
