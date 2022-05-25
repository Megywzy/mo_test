import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from Ground_truth import Ground_truth
yi=np.array([[1],[1],[1])



def projection():
    R=np.zeros((3,3))
    R[0][0] =1
    R[1][2] =-1
    R[2][1] =1

    h_3D = R @ (yi-C)

    x1 = hi_3D[0][0]
    y1 = hi_3D[1][0]
    z1 = hi_3D[2][0]


    H1 = np.zeros((2, 16))
    H1[0][0] = -fku * (1 / z1)
    H1[0][7] = -0.1 * m * fku * (1 / z1)
    H1[0][13] = fku * (1 / z1)
    H1[0][15] = -fku * x1 * z1 ** (-2)
    H1[1][14] = fkv * (1 / z1)
    H1[1][15] = -fku * x1 * z1 ** (-2)


    d = [0.01] * 2
    P_k = predictcovariance()
    Ruv = np.diag(d)
    Si = H1 @ P_k @ np.transpose(H1) + Ruv

