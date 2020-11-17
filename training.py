# Charlie Miller
# Google Kick Start - Training
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6
# Written 2020-11-16

"""
First sort the array. Then iterate over it:
maintain a rolling sum of a window, except
the sum is the difference of every element
from the last in the window. Return the smallest
rolling sum seen. 
"""

def min_hours(skills,P):
    #first sort
    skills.sort()
    #initialize the rolling sum, getting the skill diff from the
    #best player that would be on the team
    hours = sum([skills[P-1] - s for s in skills[:P]])
    min_hours = hours
    
    for i,s in enumerate(skills[P:]):
        #adjust i to be correct for global position
        i += P
        #remove skill training required for the member
        #who was removed from the window
        hours -= (skills[i-1] - skills[i-P])
        #find out the diff btw last team's best player and this team's
        diff = s - skills[i-1]
        #with this diff, that's how much more the whole team will
        #have to train to catch up
        hours += (diff * (P-1))
        min_hours = min(min_hours,hours)
        
    return min_hours


if __name__ == "__main__":
    T = int(input())
    
    for case in range(1,T+1):
        np = [int(x) for x in input().split()]
        N,P = np[0],np[1]
        Si = [int(s) for s in input().split()]
        
        y = min_hours(Si,P)
        
        print("Case #%d: %d" % (case,y))