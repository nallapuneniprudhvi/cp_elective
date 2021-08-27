# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getallpermutations(x):
	stri = ""
	return permutation(x,stri,l1=[])


def permutation(res,ans,l1):
	if len(res) == 0:
		l2 = []
		for i in ans:
			l2.append(i)
		t = tuple(l2)
		l1.append(t)
	for i in range(len(res)):
		ch = res[i]
		left = res[0:i]
		right = res[i+1:]
		resu = left + right
		permutation(resu,ans+ch,l1)
	return l1