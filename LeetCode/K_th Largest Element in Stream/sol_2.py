import heapq  # Importing the heapq module for heap operations

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with 'k' and a list of integers.

        Parameters:
        k (int): The position of the largest element to find in the stream.
        nums (List[int]): The initial stream of numbers.
        """
        self.stream = nums  # Store the input list 'nums' as the stream of numbers
        self.k = k  # Store the 'k' value
        heapq.heapify(self.stream)  # Convert the list 'nums' into a min-heap
        
        # Ensure the heap only contains the k largest elements
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)  # Remove the smallest element until the heap size is 'k'

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Parameters:
        val (int): The new value to be added to the stream.

        Returns:
        int: The kth largest element in the stream after adding the new value.
        """
        heapq.heappush(self.stream, val)  # Add the new value to the heap
        
        # Ensure the heap contains only the k largest elements
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)  # Remove the smallest element if heap size exceeds 'k'
        
        return self.stream[0]  # The root of the heap (index 0) is the kth largest element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
