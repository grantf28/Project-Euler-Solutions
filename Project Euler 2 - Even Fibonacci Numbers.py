import functools
from functools import lru_cache

@lru_cache(10000)
def evenfib(n):
    for j in range(1):
        x= n
        z =[1, 2]#Fib list
        s =2
    while(z[-1]+z[-2]<=x):
        z.append(z[-2]+z[-1]) #Append Fibonacci Numbers to list
        if(z[-1]%2 == 0): #Check If Even
            s+=z[-1]
    print(s)

