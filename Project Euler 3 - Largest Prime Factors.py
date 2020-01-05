import math 
#Function To Print Highest Prime Factor
#Project Euler #3
def primeFactors(n): 
    maxN = [] 
    #Append list with two's that divide n 
    while n % 2 == 0: 
        maxN.append(2)
        n = n // 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , append i and divide n 
        while n % i== 0: 
            maxN.append(i)
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        maxN.append(n)
    #Print Max number in list
    print(max(maxN))
    
n = int(input())
primeFactors(n)
