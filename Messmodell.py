import numpy as np
from numpy import diff
from sympy import  Matrix
import math
from prediction import predictcovariance

fku=195
fkv=195
U0=162
V0=125
K1=6*1e-06
R =np.zeros((3,3))
R[0][0] =1
R[1][2] =-1
R[2][1] =1



m=0
while m<1 :
    yi_3D=np.matrix ([[1,1.5,2,2.5],[1,1,1,1],[1,1,1,1]])
    r=np.matrix([[0.1*m],[0],[0]])
    m=m+1
    for n in range(0,4):
        yi=yi_3D[:,n]
        n=n+1
        h_3D=R @ (yi-r)

        x=h_3D[0][0]
        y=h_3D[1][0]
        z=h_3D[2][0]
        U=U0+fku*(x/y)
        V=V0+fkv*(y/z)
        r_quadrat=(fku*(x/y))**2+(fkv*(y/z))**2
        Ud=U0+(U-U0)/math.sqrt(1+2*K1*r_quadrat)
        Vd=V0+(V-V0)/math.sqrt(1+2*K1*r_quadrat)
        h= np.zeros((2, 1))
        h[0][0] = Ud
        h[1][0] = Vd
        print(h)
        H=np.zeros((2,25))
        H[0][0] = -fku * (1 / z)
        H[0][7] = -0.1* m *fku * (1 / z)
        H[0][13]= fku * (1 / z)
        H[0][15]=-fku*x*z**(-2)
        H[1][14]= fkv * (1 / z)
        H[1][15] = -fku * x * z ** (-2)
        H[0][16] = fku * (1 / z)
        H[0][18] = -fku * x * z ** (-2)
        H[1][17] = fkv * (1 / z)
        H[1][18] = -fku * x * z ** (-2)
        H[0][19] = fku * (1 / z)
        H[0][21] = -fku * x * z ** (-2)
        H[1][20] = fkv * (1 / z)
        H[1][21] = -fku * x * z ** (-2)
        H[0][22] = fku * (1 / z)
        H[0][24] = -fku * x * z ** (-2)
        H[1][23] = fkv * (1 / z)
        H[1][24] = -fku * x * z ** (-2)

        d=[0.01]*2
        P_k=predictcovariance()
        Ruv= np.diag(d)
        Si=H @ P_k @ np.transpose(H)+Ruv

##import symengine
 #vars = symengine.symbols('1 2') # Define x and y variables
 #f = symengine.sympify(['5', '7']) # Define function
 #J = symengine.zeros(len(f),len(vars)) # Initialise Jacobian matrix

 # Fill Jacobian matrix with entries
# for i, fi in enumerate(f):
    #for j, s in enumerate(vars):
         #J[i,j] = symengine.diff(fi, s)

#Si =Si+ dhi_by_dxv * Pxx * dhi_by_dxv.transpose()+ dhi_by_dxv * Pxyi * dhi_by_dyi.transpose();
  #SiRES_ += Temp_MM1;

  #SiRES_ += Temp_MM1.transpose();

  ##SiRES_ += dhi_by_dyi * Pyiyi * dhi_by_dyi.transpose();

  #SiRES_ += Ri;
