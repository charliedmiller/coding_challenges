# Charlie Miller
# Leetcode - 1291. Sequential Digits
# https://leetcode.com/problems/sequential-digits/

"""
There are only sequential numbers up to 10^9
There are 9 possible number of digits you can have
for each number up to 10^9 [1 - 9], for each there's
10 - (number of digits) seqential numbers. Here, we loop over
number of digits, and the sequentials (adding 11* for each
digit) and add them to the sequence
"""

class Solution:
    #for number of digits, get the first sequential 
    # (will always start with 1)
    def get_first_sequential(self,digits):
        cur_num = 0
        for digit in range(1,digits+1):
            exp = digits - digit
            cur_num += digit * (10 ** exp)
            
        return cur_num
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
#       outer loop will start at number of digits for the lower number,
#       and end beyond the places for the higher number
        low_places = len(str(low))
        high_places = len(str(high))
        sequence = []
        
            
        cur_digits = low_places
        while cur_digits <= high_places:
            
            #start with the first sequential for the number of digits
            cur_num = self.get_first_sequential(cur_digits)
            adder = int("1" * cur_digits)

            #there only exits 10 - cur_digits sequentials            
            digit_sequences = 10 - cur_digits
            for _ in range(digit_sequences):
                #we've gone too far, break now
                if cur_num > high:
                    break
                    
                #do not add if it's below the sequntial (will only happen a few times)
                if cur_num >= low:
                    sequence.append(cur_num)
            
                #to get next sequential, we add 1* per number of digits
                cur_num += adder
                
            cur_digits += 1
            
        return sequence