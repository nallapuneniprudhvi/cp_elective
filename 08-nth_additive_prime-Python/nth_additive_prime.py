# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isPrime(n):
	if n<2 or (n%2 == 0 and n!=2):
		return False
	if n == 2:
		return True
	else:
		for i in range(3,n//2,2):
			if n%i == 0:
				return False
		return True

def numSum(n):
	rem = 0
	sum = 0
	while n>0:
		rem = n%10
		sum += rem
		n = n//10
	return sum

def isadditiveprime(n):
	if isPrime(n) and isPrime(numSum(n)):
		return True
	return False

def fun_nth_additive_prime(n):
	count = 0
	num = 3
	if n == 0:
		return 2
	while n!=count:
		if isadditiveprime(num):
			count+=1
		num+=1
	return num-1

print(fun_nth_additive_prime(1))