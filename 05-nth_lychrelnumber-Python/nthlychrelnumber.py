# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def lychrel(n):
	for i in range(50):
		n = n+int(str(n)[::-1])
		if n == int(str(n)[::-1]):
			return False
	return True

def nthlychrelnumbers(n):
	# your code goes here
	count = 1
	num = 197
	if n == 1:
		return 196
	while count < n:
		if lychrel(num):
			count+=1
		num+=1
	return num-1