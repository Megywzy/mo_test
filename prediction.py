import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Ground_truth import Ground_truth
import numpy as np
from numpy import diff
from sympy import  Matrix
from Update import Update

def prediction():

    Xv_new=Update()[0]
    V=np.zeros((13,1))
    V[0][0] = X_v[7:, :]
    V[1][0] = X_v[8:, :]
    Xv_new= Xv+DT*V
    return (Xv_new)


def predictcovariance():
    F_n= np.zeros((16,10))
    F_n[0][0] = 0.1
    F_n[1][0] = 0.1
    F_n[7][0] = 1
    F_n[8][0] = 1

    Q=np.zeros((10,10))
    Q[0][0]=0.0001
    Q[1][1]=0.0001
    Q[2][2]=0.0001
    F_nt= np.transpose(F_n)
    Q_v=F_n @ Q @ F_nt
    P_k= Q_v
    F_x= np.zeros((16,16))
    F_x[0][0]=1
    F_x[1][1]=1

    F_x[7][7]=1
    F_x[8][8]=1

    F_x[0][7]=0.1
    F_x[1][8]=0.1

    F_xt= np.transpose(F_x)
    P_k= F_x @ P_k @ F_xt + Q_v
    return(P_k)
