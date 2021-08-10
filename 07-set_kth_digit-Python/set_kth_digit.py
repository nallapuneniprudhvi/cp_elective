# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	lis = list(str(n))
	if len(lis) == k:
		lis.insert(len(lis)-k,str(d))
	else:
		lis[len(lis)-k-1] = str(d)
	num = int("".join(lis))
	if(n>0):
		return num
	else:
		return -1*num

print(fun_set_kth_digit(468, 3, 1))