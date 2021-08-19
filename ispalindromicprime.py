def isPalindromicPrime(n):
    if isPalindrome(n) and isPrime(n):
        return True
    return False

def isPrime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    else:
        for i in range(3,(n//2)+1):
            if n%i == 0:
                return False
        return True
    
def isPalindrome(n):
    if n==int(str(n)[::-1]):
        return True
    return False


assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")