# Charlie Miller
# Leetcode - 1010. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Written 2020-12-08

"""
This is an augmented target sum: How pairs many in the array
add up to target sum X? Though we here we care about those that
add up to a multiple of 60. So first we can mod every number by 60
Since there can be duplicates we take note of the frequency for each
modded number. Like target sum, find which numbers add up to 60. For 
each pair found, multiply the freqs. 2 special cases: 60 and 30. For 
these we find the freq of 60/30 choose 2 and add it to total - since
we choose 2 to be in a pair
Time O(n) (we sort freqs, but max 60 different values to sort)
Space O(n)
"""

class Solution:
    def get_freq(self,arr):
        freqs = defaultdict(int)
        for num in arr:
            freqs[num] += 1
            
        return freqs
    
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        #edge case: there are no times
        if not time:
            return 0
        
        #get the frequency of the mod 60'd values for times
        total = 0
        songs_modded = [song_time % 60 for song_time in time]
        freqs = self.get_freq(songs_modded)
        
        #choose 2 of the numbers that can be combined with itself to add up to 60
        self_pairs = [0,30]
        for sp in self_pairs:
            #no need to check if in freqs bc of defaultdict :)
            total += math.comb(freqs[sp],2)
            del freqs[sp]
            
        #prepare for target sum - list out freq and sort by duration (mod 60)
        songs_ordered = [(dur,freq) for dur,freq in freqs.items()]
        songs_ordered.sort()
        
        #init indexes
        left = 0
        right = len(songs_ordered) -1
        
        while left < right:
            #unpack values
            left_runtime,left_amt = songs_ordered[left]
            right_runtime,right_amt = songs_ordered[right]
            
            #see what the runtime is if we combine these songs
            pair_runtime = left_runtime + right_runtime
            
            if pair_runtime > 60:
                #too long - get a shorter song from the right
                right -= 1
            elif pair_runtime < 60:
                #too short - get a longer song from the left
                left += 1
            else:
                #found a match. multiply frequencies to emulate choices
                total += left_amt * right_amt
                #advance both pointers
                left += 1
                right -= 1
                
        return total