class KthLargest:
    # Class attributes
    largest: List[int] = 0  # This will store the k largest elements
    k = 0  # This will store the value of k

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with 'k' and a list of integers.

        Parameters:
        k (int): The position of the largest element to find in the stream.
        nums (List[int]): The initial stream of numbers.
        """
        self.k = k  # Store the value of 'k'
        nums.sort()  # Sort the list of numbers
        self.largest = nums[-k:]  # Keep only the k largest elements from the sorted list

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Parameters:
        val (int): The new value to be added to the stream.

        Returns:
        int: The kth largest element in the stream after adding the new value.
        """
        # If the current number of elements is less than 'k', simply add the value
        if len(self.largest) < self.k:
            self.largest.append(val)  # Add the new value to the list
            self.largest.sort()  # Sort the list to maintain order
            return self.largest[0]  # Return the smallest element, which is the kth largest

        # If the new value is smaller than or equal to the smallest in the k largest, return the current kth largest
        if val <= self.largest[0]:
            return self.largest[0]

        # Otherwise, add the new value, sort, and remove the smallest element
        self.largest.append(val)  # Add the new value
        self.largest.sort()  # Sort the list to maintain order
        self.largest = self.largest[1:]  # Remove the smallest element to keep only 'k' elements
        return self.largest[0]  # Return the new kth largest element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
