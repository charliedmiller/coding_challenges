# Charlie Miller
# Google Kick Start - Boring Numbers
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043b0c6
# Written 2020-12-02

"""
The number of boring numbers in the set of all numbers with
x digits is 5^x. Add for all digits leading up to number in
question. For the remainder, determine how many boring numbers
there are leading up to each digit. Using aforementioned formula, this
can be calculated per digit
"""

def boring_numbers_upto(num):
    count = 0
    num_str = str(num)
    digits = len(str(num))

    #add up boring numbers found in all digits leading up to
    # number of digits number actually has
    #this can be in a formula, but max digits is 19, so this is acceptable
    for digit in range(1,digits):
        count += 5**digit

    #swich between expecting odd or not odd
    expecting_odd = True
    for digit_idx in range(0,digits):
        #examine digits left to right, determine their value
        digit_val = int(num_str[digit_idx])

        #determine how many borings are found per 100, 1000 etc
        #number of zeros based off current digit
        exp = digits - digit_idx - 1
        borings_per = 5**exp

        #how many we add goes according to if we're expecting an odd here,
        #if this is the first digit in the number,
        #and what the value of the digit is
        if expecting_odd:
            #how many to add if odd
            count += borings_per * (digit_val//2)
        elif digit_idx == 0:
            #how many to add if even and it's the first digit
            count += borings_per * ((digit_val-1)//2)
        else:
            #how many to add if even and it's not the first digit
            count += borings_per * ((digit_val+1)//2)

        #if this digit was the wrong digit for boring, we stop here
        digit_odd = digit_val % 2 != 0
        if digit_odd != expecting_odd:
            break

        #if this is the last digit, add it to the total
        if digit_idx == (digits-1):
            count += 1

        #switch to the opposite according to the problem
        expecting_odd = not expecting_odd

    return count
            

def boring_numbers(left,right):
    #this is equivalent to finding how many fall in the range
    return boring_numbers_upto(right) - boring_numbers_upto(left-1)


if __name__ == "__main__":
    T = int(input())

    for case in range(1,T+1):
        lr = [int(x) for x in input().split()]
        res = boring_numbers(lr[0],lr[1])

        print("Case #%d: %d" % (case,res))
