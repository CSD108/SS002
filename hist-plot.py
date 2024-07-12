import numpy as np
import matplotlib.pyplot as plt

with open("samples_array_0.txt","r") as file:
    lst = [float(line) for line in file]
qc = [-0.017186958333333335 , -0.009313458333333332 , -0.003240083333333333 , 0.0020190833333333332 , 0.00679025 , 0.011591916666666667 , 0.01734983333333334] 
v = ['violet','indigo','blue','green','yellow','orange','red']
plt.hist(lst,bins=200,color='c')
plt.xlim(-0.055,0.057)
plt.xlabel("Sample value (in V)")
plt.ylabel("Frequency of sample")
plt.title("Normal distribution of samples")
for q in range(len(qc)):
    plt.axvline(qc[q],color=v[q],linewidth=1,linestyle='-')

plt.show()