# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def col_sum(col,arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i][col]
	return sum

def ismostlymagicsquare(a):
	if len(a) == 1:
		return True
	sum_r = 0
	sum_l = 0
	sum_col_lis = []	
	sum_row_lis = []
	for i in range(len(a)):
		sum_row = 0
		sum_col = 0
		for j in range(len(a[0])):
			if i == j:
				sum_r  += a[i][j]
			if i+j == len(a)-1:
				sum_l += a[i][j]
			sum_row += a[i][j]
		sum_row_lis.append(sum_row)
		sum_col_lis.append(col_sum(i,a))
	if len(set(sum_row_lis)) != 1 or len(set(sum_col_lis)) != 1:
		return False
	if sum_l != sum_r:
		return False
	return True

	# Your code goes here
