# Write the function getInRange(x, bound1, bound2) which takes 3 int values
# x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
# If x is between the two bounds, just return it unmodified. Otherwise, 
# if x is less than the lower bound, return the lower bound, 
# or if x is greater than the upper bound, return the upper bound.

def fun_getinrange(x, bound1, bound2):
	min_num = min(bound1,bound2)
	max_num = max(bound1,bound2)
	if x <= max_num and x >= min_num:
		return x
	elif x> max_num:
		return max_num
	elif x < min_num:
		return min_num
	# your code goes here
print(fun_getinrange(4, 3, 5))