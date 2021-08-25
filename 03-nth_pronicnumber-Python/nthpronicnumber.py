# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(n):
    flag=False
    for i in range(n):
        if i *(i+1)==n:
            flag=True
            break
    return flag==True
 
def nthpronicnumber(n):
    count=1
    num=0
    while(count<=n):
        num+=1
        if(pronicnumber(num)):
            count+=1
    return num
