#Homework 1
#Tarik Dahnoun

import numpy as np
import pylab

def position(x0,u,v0,t,m0,p):
    X=x0+(u+v0)*t+u*(m0/p-t)*np.log(1-p*t/m0)
    return X
    
def velocity(u,v0,t,m0,p):
    V=v0-u*np.log((m0-p*t)/m0)
    return V

def root_finder(a,b,x0,u,v0,m0,p):
    c=(a+b)/2
    
    while np.absolute(a-b)>=.001:
        if np.sign(position(x0,u,v0,c,m0,p)-4000)==np.sign(position(x0,u,v0,a,m0,p)-4000):
            a=c
        elif np.sign(position(x0,u,v0,c,m0,p)-4000)==np.sign(position(x0,u,v0,b,m0,p)-4000):
            b=c
        c=(a+b)/2
    return a
    
a=2
b=10.0
x0=0. #m
u=2000. #m/s
v0=0. #m/sk
m0=5000. #kg
p=200. #kg/s
xmax=4000.0
A=root_finder(a,b,x0,u,v0,m0,p) #time
B=velocity(u,v0,A,m0,p) #velocity
M=m0-p*A #mass
print "The time it will take for the rocket to reach 4000m is", A, "seconds"
print "At this time, the rocket is going", B, "meters per second"
print "And it weighs", M, "kilograms"


tmin=a
tmax=b
nts=100
ti=np.linspace(tmin,tmax,nts)
y=position(x0,u,v0,ti,m0,p)
v=velocity(u,v0,ti,m0,p)
m=m0-p*ti

pylab.plot(ti,y,'.-',label=r"Position")
pylab.plot(ti,v,'.-',label=r"Velocity")
pylab.plot(ti,m,'.-',label=r"Mass")
pylab.xlabel("Time [s]",fontsize=16)
pylab.ylabel("Position [m]",fontsize=16)
pylab.axhline(0,color='k',ls='--')
pylab.axvline(A,color='k',ls='--',label=r"x=4000")

pylab.title("x=4000 at Verticle Line")
pylab.show()

pylab.legend(loc='top',fontsize=11)