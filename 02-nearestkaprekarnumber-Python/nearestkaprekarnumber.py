# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def kaprekar(n):
    num_square = n**2
    len_n = len(str(num_square))
    count = 0
    while count < len_n:
        count += 1
        parts = 10**count
        if parts == n:
            continue
        sumi = (num_square//parts) + (num_square%parts)
        if sumi == n:
            return True
    return False

def fun_nearestkaprekarnumber(n):

    flag = False
    num1 = n-1
    num2 = n+1
    while(flag!=True):
        if(kaprekar(n)==True):
            return n
        if(kaprekar(num1)==True):
            return num1
        if(kaprekar(num2) == True):
            return num2
        num1 -= 1
        num2 += 1