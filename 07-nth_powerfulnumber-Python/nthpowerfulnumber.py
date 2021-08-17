# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isPrime(n):
	if n == 2 or n==3:
		return True
	if n%2 == 0:
		return False
	for i in range(3,n//2+1,2):
		if n%i == 0:
			return False
	return True


def powerful(n):
	if (n**(0.5)%int(n**(0.5)) == 0) or (n**(1/3)%int(n**(1/3)) == 0):
		return True
	else:
		if isPrime(n):
			return False
		for i in range(2,int(n**0.5)+1):
			count = 0
			while n%i == 0:
				n = n//i
				count += 1
			if count==1 :
				return False
		return n==1

print(powerful(20))


def nthpowerfulnumber(n):
	# Your code goes here
	count = 0
	num = 1
	while count <= n:
		if powerful(num):
			print(num)
			count+=1
		num+=1
	return num-1

print(nthpowerfulnumber(19))