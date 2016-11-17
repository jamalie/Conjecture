#   Consider the following algorithm to generate a sequence of numbers. Start with an integer n.
#   If n is even, divide by 2. If n is odd, multiply by 3 and add 1.
#   Repeat this process with the new value of n, terminating when n = 1.
#   For example, the following sequence of numbers will be generated for n = 22:

#   22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#   It is conjectured (but not yet proven) that this algorithm will terminate at n = 1 for every integer n.
#   Still, the conjecture holds for all integers up to at least 1, 000, 000.
#   For an input n, the cycle-length of n is the number of numbers generated up to and including the 1. In the example above,
#   the cycle length of 22 is 16. Given any two numbers i and j,
#   you are to determine the maximum cycle length over all numbers between i and j, including both endpoints.

def conjecture(i, j):
    count = 0
    nMax = [0,0]
    currentI = 0

    for i in range(i,j,1):
        currentI = i
        if i < 1:
            return 0
        while(i!=1):
            if i%2 == 0:
                i /=2
                count +=1
            else:
                i = i*3
                i = i+1
                count +=1

        count+=1
        if count > nMax[1]:
            nMax[0] = currentI
            nMax[1] = count

        count = 0

    return nMax

print conjecture(100,200)