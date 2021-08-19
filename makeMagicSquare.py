# makeMagicSquare(n)
# Write the function makeMagicSquare(n) that takes a positive 
# odd integer n and returns an nxn magic square by following 
# the resource here. If n is not a positive odd integer, 
# return None.

# URL: https://en.wikipedia.org/wiki/Magic_square

# Hints: From Geeks for Geeks.
# Did you find any pattern in which the numbers are stored? 

# In any magic square, the first number i.e. 1 is 
# stored at position (n/2, n-1). Let this position 
# be (i,j). The next number is stored at position (i-1, j+1) 
# where we can consider each row & column as circular array 
# i.e. they wrap around.

# Three conditions hold:

# 1. The position of next number is calculated by 
# decrementing row number of the previous number by 1,
#  and incrementing the column number of the previous 
# number by 1. At any time, if the calculated row position 
# becomes -1, it will wrap around to n-1. Similarly, if 
# the calculated column position becomes n, it will wrap 
# around to 0.

# 2. If the magic square already contains a number at the 
# calculated position, calculated column position will be 
# decremented by 2, and calculated row position will be 
# incremented by 1.

# 3. If the calculated row position is -1 & calculated 
# column position is n, the new position would be: (0, n-2). 

def makeMagicSquare(n):
    # Your code goes here...
    if n <= 0:
        return None
    matrix= [[0 for i in range(n)]for j in range(n)]
    i = n//2
    j = n-1
    val = 1
    len_mat = n*n
    while val <=len_mat:
        if matrix[i][j]:
            j -= 2
            i+=1
            continue
        else:
            matrix[i][j] = val
            val+=1
        j += 1
        i -= 1
        if i == -1 and j == n:
            j= n-2
            i = 0
        else:
            if j == n:
                j = 0
            if i< 0:
                i = n-1
    return matrix

assert(makeMagicSquare(3) == [[2, 7, 6], [9, 5, 1], [4, 3, 8]])
assert(makeMagicSquare(5)== [[9, 3, 22, 16, 15], [2, 21, 20, 14, 8], [25, 19, 13, 7, 1], [18, 12, 6, 5, 24], [11, 10, 4, 23, 17]])
assert(makeMagicSquare(0) == None)
print("All test cases passed..!!")
