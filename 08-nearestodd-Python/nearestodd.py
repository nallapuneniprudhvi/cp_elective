# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	num = int(n)
	if num%2==0 and num == n:
		return num-1
	elif num%2!=0:
		return num
	elif num%2==0:
		return num+1

