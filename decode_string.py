# Charlie Miller
# Leetcode - 394. Decode String
# https://leetcode.com/problems/decode-string/
# Written 2020-11-19

"""
Iterate over the string. If it's an alpha, just add it
Otherwise extract the number. If there's a bracket, extract
everything inside. To account for nesting, also keep track of 
how many open/close brackets we encounter, we end when all
opened brackets are now closed. Otherwise discard the number
Recursively solve this problem for the extracted string inside the
bracket
"""

class Solution:
    def decodeString(self, s: str) -> str:
        #edge case: no valid string
        if not s:
            return ""
        
        #our string builder here
        decoded = ""
        i = 0
        
        while i < len(s):
            #if a real character, just add it!
            char = s[i]
            if char.isalpha():
                decoded += char
            #encountered a number
            else:
                #extract the number
                j = i
                while j < len(s) and s[j].isnumeric():
                    j += 1
                    
                #encountered number at the end of the string. Just discard
                if j > len(s):
                    break
                
                #convert extracted number
                multiplier = int(s[i:j])
                
                #only add a string if followed by a bracket
                if s[j] == "[":
                    #extract the string inside the brackets
                    open_ctr = 0
                    k = j+1
                    while open_ctr != 0 or s[k] != "]":
                        #do not break at the first sight of "]" if 
                        #we encounter a "[" before. there's a nested
                        #bracket!! Make sure all nested brackets are closed
                        if s[k] == "[":
                            open_ctr += 1
                        elif s[k] == "]":
                            open_ctr -= 1
                        
                        k += 1
                    
                    #nested string
                    nested_encoded = s[j+1:k]
                    nested_decoded = self.decodeString(nested_encoded)
                    #generate the string according to the decoded and the multipier
                    decoded += (nested_decoded * multiplier)
                    
                    i = k
                else:
                    #shift left because j is already at the next character
                    i = j-1
                    
            i += 1
            
        return decoded
        