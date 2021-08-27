# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    # Your code goes here
    if isPrime(n) and ishappy(n):
        return True
    return False

def ishappy(n):
    if(n==1):
        return True
    while (n>=10):
        lis = list(map(int,str(n)))
        sq = sum([i**2 for i in lis])
        n=sq
        if(n==1):
            return True
    return False

def isPrime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    for i in range(3,n//2,2):
        if n%i == 0:
            return False
    return True

print(ishappy(2))