from statistics import mean
import numpy as np
import math
rho0=0.5
k0=0.5
n0=3
x=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90])
y=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
base=sum((y-mean(y))**2)
for i in range(1,101)
 for j in range(1,101)
  for k in range(1,101)
   rho1 = 
def brdffunction(canshu,x)
    BRDF_rho = canshu[1]
    BRDF_k = canshu[2]
    BRDF_n = canshu[3]
    L=x(1)
    N = x[10:12]
    V = x[13:15]
    H = x[16:18]
    theta=vAngle(L,H)
    alpha=x[6]
    F=F_factor(theta,BRDF_n)
    D=D_factor(alpha,BRDF_rho)
    G=G_factor(L,N,V,H)
    return (F*D*G/((2*math.pi)*(sum())

