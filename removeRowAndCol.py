# removeRowAndCol (non-destructive and destructive)
# Here we will write removeRowAndCol(row, col), 
# Do not use copy.deepcopy and directly construct 
# the modified 2d list.

# The function takes a rectangular list L and two ints, 
# row and col. the goal is to obtain a version of the list 
# that has the given row and given column removed. 
# You may assume that row and col are both legal values 
# (that is, they are non-negative integers that are smaller 
# than the largest row and column, respectively). For example, 
# the list shown to the left would lead to the result shown on 
# the right when called with row 1 and column 2.

# list
# [ [ 2, 3, 4, 5],
#   [ 8, 7, 6, 5],
#   [ 0, 1, 2, 3] ]

# result
# [ [ 2, 3, 5],
#   [ 0, 1, 3] ]

def removeRowAndCol(L, row, col):
    # Your code goes here...
    lis = []
    for i in range(len(L)):
        lis1 = []
        for j in range(len(L[0])):
            if(i == row):
                break
            if i != row and j!=col:
                lis1.append(L[i][j]) 
        if(len(lis1)>0):
            lis.append(lis1)

    return lis

# Write your own test cases.
assert removeRowAndCol([ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]],1,2)==[[2, 3, 5], [0, 1, 3]]
assert removeRowAndCol([ [ 1,3,5,7],[ 2,4,6,8],[1,4,7,0]],1,2)==[[1,3,7], [1,4,0]]
assert removeRowAndCol([ [ 11,33,55,77],[ 22,44,66,88],[ 11,44,77,00]],1,3)==[[11,33,55], [11,44,77]]
assert removeRowAndCol([ [-1,-2,-4,-6],[-11,-53,-37,-29],[ 134,23,657,546]],0,1)==[[-11,-37,-29], [134,657,546]]
print("All test cases passed...!!!")