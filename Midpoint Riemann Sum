#Homework 2
#Tarik Dahnoun

#Computes the Riemenn Sum using midpoints

import numpy as np

a=0
b=100

N1=10000
N2=25000
N3=100000

def func(x):
    y=np.sin(x**2)
    return y
    
def analytic(): #from wolfram
    return .631418
A=analytic()

def midpoint(n):
    x=np.linspace(a,b,n,endpoint=False)
    I=np.zeros(n)
    dt=x[1]-x[0]
    
    for i in range(n):
        I[i]=func(x[i]+dt/2)*dt
    I.tolist()
    II=sum(I)
    return II

I1=midpoint(N1)
I2=midpoint(N2)
I3=midpoint(N3)

count1=1500
while abs(A-midpoint(count1))>=.0001: #3 sigfigs
    count1+=1

count2=25000
while abs(A-midpoint(count2))>=.00001: #4 sigfigs
    count2+=1

count3=85000
while abs(A-midpoint(count3))>=.000001: #5 sigfis
    count3+=1

print "      TABLE"
print "___________________"
print "N Values|Integral"
print count1,"   ",I1, "    ->This is accurate to 3 sigfigs"
print count2,"   ",I2, "    ->This is accurate to 4 sigfigs"
print count3,"  ",I3, "    ->This is accurate to 5 sigfigs"
