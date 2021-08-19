# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


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

print(kaprekar(999))

def fun_nth_kaprekarnumber(n):
    count = 0
    num = 1
    while count <= n:
        if kaprekar(num):
            print(num)
            count+=1
        num +=1
    return num-1

print(fun_nth_kaprekarnumber(0))