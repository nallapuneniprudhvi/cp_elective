# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN chessboard such that no two queens are attacking each other. For most values of N, there are many ways to solve this problem. Here, you will write the function nQueensChecker(board) that takes a 2d list of booleans where True indicates a queen is present and False indicates a blank cell, and returns True if this NxN board contains N queens all of which do not attack any others, and False otherwise.

def canqueenattack(qR, qC, oR, oC):
	if qR == oR or qC == oC or qR-oR == qC-oC:
		return True
	return False

def nQueensChecker(a):
    # Your code goes here...
    lis = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 1:
                lis.append([i,j])
   
    for i in range(len(lis)):
        
        for j in range(i+1,len(lis)):
            if canqueenattack(lis[i][0],lis[i][1],lis[j][0],lis[j][1]) == True:
                return False
    return True

lis = [[1,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,0],[0,0,0,1,0]]
assert(nQueensChecker(lis)==True)
assert(nQueensChecker(lis)!=False)
print("All test cases passed...!!")