import numpy as np
import matplotlib.pyplot as plt

dic = {0: 8452926, 1: 8252852, 2: 8315192, 3: 8229677, 4: 8258828, 5: 8249101, 6: 8554280, 7: 8370024}
height = [dic[i]/1e6 for i in dic.keys()]
height_arr = [np.round(i,2) for i in height]
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i-0.2,y[i],y[i])

plt.title("Bin Proportions")
plt.xlabel("Bin Number")
plt.ylabel("No. of Samples ($\\times 10^6$)")
plt.bar(dic.keys(),height)
addlabels(dic.keys(),height_arr)
plt.show()