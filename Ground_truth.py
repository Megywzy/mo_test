import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def Ground_truth():
    DT = 1  # time tick [s]
    t= 50  # simulation time [s]
    X_vinit=np.array([[10],[10],[0],[1],[0],[0],[0],[1],[0],[0],[0],[0],[0]])

    v=np.array([[1],[1],[0]])
    Xv = X_vinit
    Xv=Xv+np.array([[v[0,:]*DT],[v[1,:]*DT],[0],[1],[0],[0],[0],[1],[0],[0],[0],[0],[0]], dtype="object")
    return(Xv)
    q=np.array([[1],[0],[0],[0]])
    w=np.array([[0],[0],[0]])



    list_x = []
    list_y = []

    n=0
    while n < t+1:

        X_v=np.array( [[X_vinit[0, :] + v[0, :] * DT*n], [X_vinit[1, :] + v[1, :] * DT*n], [0], [1], [0], [0], [0], [1], [0], [0],[0], [0], [0]], dtype="object")

        x = X_v[0,:]
        y = X_v[1, :]

        n = n + 1
        list_x.append(x)
        list_y.append(y)





    fig=plt.figure()
    ax = Axes3D(fig,auto_add_to_figure=False)

    fig.add_axes(ax)

    plt.figure(figsize=(10,10))
    plt.subplot(1,1,1)
    plt.xlim((0,70))
    plt.ylim((0,70))
    ax.set_zlim(0,70)
    ax.scatter3D(list_x,list_y ,0,cmap='Greens', label="Groundtruth")

    plt.show()



Ground_truth()







