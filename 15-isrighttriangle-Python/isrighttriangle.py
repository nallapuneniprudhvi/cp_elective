# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = ((x2-x1)**2 + (y2-y1)**2)
	b = ((x3-x2)**2 + (y3-y2)**2)
	c = ((x3-x1)**2 + (y3-y1)**2)
	if a == b+c or b == a+c or c == a+b:
		return True
	return False
		
print(isrighttriangle(-1, 7, 10, -4, 12, -2))
