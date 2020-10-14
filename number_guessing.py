# Charlie Miller
# Kick Start - Number Guessing
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4#problem

#Do a binary search for the number
def guess_number(lower,upper,attempts):
    result = None
    
    for _ in range(attempts):
        guess = lower + (upper-lower)//2
        print(guess)
        result = input()
        if result == "WRONG_ANSWER":
            return False
            
        if result == "CORRECT":
            return True
            
        if result == "TOO_BIG":
            upper = guess
        elif result == "TOO_SMALL":
            lower = guess+1
            
    return False
            

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        A,B = tuple([int(x) for x in input().split(" ")])
        N = int(input())
        
        success = guess_number(A,B,N)
        if not success:
            break