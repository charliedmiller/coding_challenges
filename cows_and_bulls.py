# Charlie Miller
# Leetcode - 299. Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/

"""
Iterate over once to get bulls. 
Any non-bull gets put into a frequency count for bot secret and guess
Then iterate over found frequencies of the guess. 
Cows are the min of both frequencies for that number
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #initialize:both are 0
        bulls = 0
        cows = 0
        
        #initialize frequncy counts
        guess_freqs = defaultdict(int)
        secret_freqs = defaultdict(int)
        
        #iterate over once to count bulls, and the frequencies of non-bulls
        for s,g in zip(secret,guess):
            
            #bull! don't count this to frequencies
            if s == g:
                bulls += 1
                continue
                
            #add to frequencies
            guess_freqs[g] += 1
            secret_freqs[s] += 1
            
        #iterate over seen frequencies for guesses
        for guess_num,freq in guess_freqs.items():
            #cows is the overlap (min)
            cows += min(freq,secret_freqs[guess_num])
            
        #format our answer
        return "%dA%dB" % (bulls,cows)
                
            