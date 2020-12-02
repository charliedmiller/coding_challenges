# Charlie Miller
# Google Kick Start - Retype
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7
# Written 2020-12-01

def retype(n,k,s):
    base = k-1
    restart = base + n + 1
    back = k-s
    from_s = n - s + 1
    backtrack = base + back + from_s
    return min(restart,backtrack)

    

if __name__ == "__main__":
    
    T = int(input())

    for case in range(1,T+1):
        nks = [int(x) for x in input().split()]
        res = retype(nks[0],nks[1],nks[2])
        print("Case #%d: %d" % (case,res))

