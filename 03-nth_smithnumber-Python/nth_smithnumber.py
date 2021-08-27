# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


 
def fun_nth_smithnumber(n):
   count=0
   x=1
   y = 0
   while(n+1!=count):
       if(isSmith(x)):
           count+=1
           y = x
       x+=1
   return y
 
def isPrime(n):
   if (n < 2):
       return False
   if (n == 2):
       return True
   if (n % 2 == 0):
       return False
   for i in range(3,n//2+1,2):
       if (n % i == 0):
           return False
   return True
 
def isSmith(n):
   if(isPrime(n)!=True):
       val = n
       lis = []
       factors_sum=0
       res = 0
       if n==1:
           return False
       for i in range(2,(n//2) + 1):
           if(isPrime(i)==True) and (n%i==0):
               lis.append(i)
          
       for an in str(n):
           res+=int(an)
      
       li=[]
       for i in lis:
           while (val%i==0 and val!=0):
               li.append(i)   
               factors_sum+=i
               val=val//i
      
       val_final = 0       
       for j in li:
           if(j>9):
               for d in str(j):
                   val_final = val_final+int(d)
           else:
               val_final = val_final+j
      
       if(res==val_final):
           return True
       else:
           return False
