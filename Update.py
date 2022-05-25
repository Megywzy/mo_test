import numpy as np
from numpy import diff
from sympy import  Matrix
import math
from prediction import predictcovariance
from prediction import prediction
from Ground_truth import Ground_truth
def Update():
    g=mi-hi
    P_k = predictcovariance()
    W= P_k @ transpose(H1) @ inv(Si)
    Xv= Ground_truth()
    Xv= Xv+ W @ g

    Xv_new = prediction(Xv_new)
    Xv_new = Xv_new + W @ g

    P_k= P_k - W @ Si @ np.transpose(W)
    return (Xv, Xv_new,P_k)