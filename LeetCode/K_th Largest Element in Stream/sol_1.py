import heapq  # Importing the heapq module to use the heap data structure

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object.

        Parameters:
        k (int): The 'k' value representing the position of the largest element to find.
        nums (List[int]): The initial stream of numbers.
        """
        self.k = k  # Store the 'k' value
        self.min_heap = nums  # Use the input list 'nums' as the underlying heap
        heapq.heapify(self.min_heap)  # Transform the list into a heap (min-heap by default)
        
        # Ensure the heap contains only the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  # Remove the smallest element until the heap size is 'k'

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.

        Parameters:
        val (int): The new value to be added to the stream.

        Returns:
        int: The kth largest element in the stream after adding the new value.
        """
        heapq.heappush(self.min_heap, val)  # Add the new value to the heap
        if len(self.min_heap) > self.k:  # If the heap size exceeds 'k',
            heapq.heappop(self.min_heap)  # remove the smallest element to maintain the size of 'k'
        
        return self.min_heap[0]  # The root of the heap (index 0) is the kth largest element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)