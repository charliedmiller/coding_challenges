# Charlie Miller
# Leetcode - 763. Partition Labels
# https://leetcode.com/problems/partition-labels/

"""
2 passes:
first find where the last ocurrence of each character is found
second keep track of where the furthest character is found 
(it's either from a prev character, or the current character)
When we reach the furthest, we can cut off for another partition
keep track of characters included before each cut off
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #rightmost ocurrence of each letter
        rights = {}
        
        #when we encounter a character that's the right most ocurrence so far
        for i,char in enumerate(S):
            rights[char] = i
            
        # for second pass, keep track of furthest character, and how many
        # characters we've passed before making a partition
        partition_ct = 0
        furthest = -1
        partitions = []
        
        
        for i,char in enumerate(S):
            
            partition_ct += 1
            #advance furthest if new character, and it's further out
            furthest = max(furthest,rights[char])
            
            #We've reached the furthest for a partition, let's cut it off
            if i == furthest:
                partitions.append(partition_ct)
                partition_ct = 0
                
        return partitions
            