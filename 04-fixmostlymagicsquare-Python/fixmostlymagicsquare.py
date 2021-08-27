# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	row = 0
	col = 0
	flag = False
	if len(L)==1:
		return True
	for i in range(len(L)):
		for j in range(len(L)):
			row = row + L[i][j]
			col = col + L[j][i]
		if((row!=col) and flag == False):
			flag = True
			L[i][j] = L[i][j]-(row-col)
	return L