import numpy as np
import matplotlib.pyplot as plt

with open("bit-spacing.txt","r") as file:
    times = np.array([float(line) for line in file])
diff_times = np.round(np.diff(times),2)
sample = [i for i in range(len(diff_times))]

plt.ylim(0,0.15)
plt.ylabel("Time (in sec)")
plt.xlabel("Bit count")

plt.plot(sample,diff_times,'.')
plt.show()


    