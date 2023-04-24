from ast import Pow
import numpy as np
import math
import pandas as pd

def brdffunction(canshu,x):
    rho=canshu[0]
    k=canshu[1]
    n=canshu[2]
    for i in range(x.shape[0]):
        L=x[i,7:9]
        N=x[i,10:12]
        V=x[i,13:15]
        H=x[i,16:18]
        theta=vAngle(L,N)
        alpha=x[i,6]
        F=F_factor(theta,n)
        D=D_factor(alpha,rho)
        G=G_factor(L,N,V,H)
        return(F*D*G/((2*math.pi*math.pi)*(np.dot(L,N)*np.dot(N,V)))+k/math.pi)

def vAngle(A,B):
    return(math.acos(np.dot(A,B)/(math.sqrt(np.dot(A,A))*math.sqrt(np.dot(B,B)))))

def F_factor(theta,n):
    ct=math.cos(math.radians(theta))
    g=n*n+ct*ct-1
    return(0.5*pow((g-ct)/(g+ct),2)*(1+pow((ct*(g+ct)-1)/(ct*(g-ct)+1),2)))

def D_factor(a,rho):
    return(math.exp(-pow(math.tan(math.radians(a))/rho,2))/(rho*rho*pow(math.cos(math.radians(a)),4)))

def G_factor(L,N,V,H):
    G1=2*np.dot(N,H)*np.dot(N,V)/np.dot(V,H)
    G2=2*np.dot(N,H)*np.dot(N,L)/np.dot(V,H)
    return(np.min([1,np.min([G1,G2])]))


x = np.array([[], []])
y = np.array([0.05, 0.05])
rho0 = 0.5
k0 = 0.5
n0 = 3

basey = np.sum((y - np.mean(y))**2)
p1 = np.zeros(y.shape)
sse1 = 0
rsquare1 = 0

for i in range(100):
    for j in range(100):
        for k in range(100):
            rho1 = rho0 + 1 * np.power(0.1, 2) * (i - 50)
            k1 = k0 + 1 * np.power(0.1, 2) * (j - 50)
            n1 = n0 + 4 * np.power(0.1, 2) * (k - 50)
            sum1 = 0
            for m in range(y.shape[0]):
                canshu = np.array([rho1, k1, n1])
                p1[m] = brdffunction(canshu, x[m, :])
                sum1 += pow((p1[m] - y[m]), 2)
            sse1 = np.sqrt(sum1)
            rsquare1_temp = 1 - pow(sse1, 2) / basey
            if rsquare1_temp > rsquare1:
                rsquare1 = rsquare1_temp
                result1 = np.array([rho1, k1, n1, rsquare1])

p2 = np.zeros(y.shape)
sse2 = 0
rsquare2 = 0

for i in range(100):
    for j in range(100):
        for k in range(100):
            rho2 = rho1 + 2 * np.power(0.1, 4) * (i - 50)
            k2 = k1 + 2 * np.power(0.1, 4) * (j - 50)
            n2 = n1 + 8 * np.power(0.1, 4) * (k - 50)
            sum2 = 0
            for m in range(y.shape[0]):
                canshu = np.array([rho2, k2, n2])
                p2[m] = brdffunction(canshu, x[m, :])
                sum2 += pow((p2[m] - y[m]), 2)
            sse2 = np.sqrt(sum2)
            rsquare2_temp = 1 - pow(sse2, 2) / basey
            if rsquare2_temp > rsquare2:
                rsquare2 = rsquare2_temp
                result2 = np.array([rho2, k2, n2, rsquare2])

p = np.zeros(y.shape)
for i in range(y.shape[0]):
    canshu = [result2[0], result2[1], result2[2]]
    p[i] = brdffunction(canshu, x[i, :])

result = np.concatenate((result1, result2, y, p), axis=0)

