# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
	val = list(map(int,str(n**5)))
	for i in range(0,10):
		if i not in val:
			return False
	return True


def nthwithproperty309(n):
	# Your code goes here
	count = 1
	num = 310
	if n == 0:
		return 309
	while count<=n:
		num+=1
		if(property309(num)):
			count += 1
			print(count)
	return num 

print(nthwithproperty309(1))
print(property309(418))