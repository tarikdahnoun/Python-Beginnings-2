#Homework 2
#Tarik Dahnoun
#8/31/17

# Program finds the first 100 prime numbers by checking to see if, for a trial integer n, n is divisible by any of the primes found thus far.

import numpy as n
import pylab as p

primes = n.zeros(100)            
count=2
primes[0]=2     #The weird prime
primes[1]=3     #The other werid prime
num=4           #Starting point

while count<100:    #The first 100 prime numbers
    found=0  #False
    for i in n.arange(0,count+1):   #references the previous (prime) numbers in the array
        if(num%primes[i])==0:       #Checking if prime
            found=1                 #If not prime, output true
            break                   #Stop loop
    if(found)==0:                   #If prime
            primes[count] = num     #Add to array
            count=count+1           #Iterate
    num=num+1
print primes

       