import math
from math import log
from operator import mul
import functools
from functools import reduce

#Check prime numbers.
def isPrime(num):
    prim = True

    for x in range(2, num):
        if num % x == 0:
            prim = False
            break
    return prim

n= int(input("Number to check"))
primes = []
for i in range(1, n+1):
    if isPrime(i + 1):
        primes.append(i+1)#Append empty list with primes

#https://blog.dreamshire.com/project-euler-5-solution/
print(reduce(mul, (p ** int(log(n)/log(p)) for p in primes), 1)) #Determine exponent of the prime
#Instead of reduce and mul
# a = 1
# for p in primes:
#     a*= p**int(log(n)/log(p))

			