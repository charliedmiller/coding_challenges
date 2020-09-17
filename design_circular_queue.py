# Charlie Miller
# Leetcode - 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

"""
Keep track of front and back pointers. Back actually represents
1 more than the location of the last.
As a result, we must have a sentinel array space so we can tell
the difference for when array is full (back at sentinel),
and array is empty (back at first)
"""

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k+1
        self.arr = [None] * (k+1)
        self.front = 1
        self.back = 1
        self.sentinel = 0
        
    def increment(self,index):
        return (index +1) % self.size
    
    def decrement(self,index):
        return (index -1) % self.size
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        self.arr[self.back] = value
        self.back = self.increment(self.back)
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        self.front = self.increment(self.front)
        self.sentinel = self.increment(self.sentinel)
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        
        return self.arr[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        
        return self.arr[self.decrement(self.back)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.back
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return  self.back == self.sentinel
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()