# Charlie Miller
# Leetcode - 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/

"""
Maintain a queue of ping times
Dequeue any times before t - 3000
Count how many are in the queue
"""

class RecentCounter:

    def __init__(self):
        self.call_queue = []

    def ping(self, t: int) -> int:
        #add current time to queue (as specified by problem)
        self.call_queue.append(t)

        #dequeue any times in queue before time t - 3000
        prev_time = t - 3000
        while prev_time > self.call_queue[0]:
            self.call_queue.pop(0)
            
        return len(self.call_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)