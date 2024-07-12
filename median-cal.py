import numpy as np
import matplotlib.pyplot as plt
med_lst = []
med_1 = []
med_2 = []
med_3 = []
med_4 = []
med_5 = []
med_6 = []
med_7 = []
for i in range(6,30):
    with open(f"samples_array_{i*10}.txt","r") as file:
        lst = np.array( [float(line) for line in file])
    #    print(lst[0])
        file.close()
    sorted_lst = np.sort(lst)
    #print(sorted_lst[0])
    med_lst = [sorted_lst[j*61440] for j in range(0,8)]
    #print(med_lst[0])
    t = [i*10 for i in range(6,30)]
    med_1 += [med_lst[1]]
    med_2 +=[ med_lst[2]]
    med_3 +=[ med_lst[3]]
    med_4 +=[ med_lst[4]]
    med_5 +=[ med_lst[5]]
    med_6 +=[ med_lst[6]]
    med_7 +=[ med_lst[7]]

med_arr_1 = [i*1000 for i in med_1]
med_arr_2 = [i*1000 for i in med_2]
med_arr_3 = [i*1000 for i in med_3]
med_arr_4 = [i*1000 for i in med_4]
med_arr_5 = [i*1000 for i in med_5]
med_arr_6 = [i*1000 for i in med_6]
med_arr_7 = [i*1000 for i in med_7]
plt.title("Quantile indices evolution")
plt.xlabel("Time (in minutes)")
plt.ylabel("Quantile index (Q-ind) value (in mV)")

plt.plot(t,med_arr_1,'purple')
plt.plot(t,med_arr_2,'indigo')
plt.plot(t,med_arr_3,'b')
plt.plot(t,med_arr_4,'g')
plt.plot(t,med_arr_5,'y')
plt.plot(t,med_arr_6,'orange')
plt.plot(t,med_arr_7,'r')
plt.plot([60,60],[-18,18],'k')
plt.legend(['Q-ind-1','Q-ind-2','Q-ind-3','Q-ind-4','Q-ind-5','Q-ind-6','Q-ind-7','Q-start'],loc='upper right')#, bbox_to_anchor=(1, 0.5))
plt.show()
q1 = np.mean(med_1)
q2 = np.mean(med_2)
q3 = np.mean(med_3)
q4 = np.mean(med_4)
q5 = np.mean(med_5)
q6 = np.mean(med_6)
q7 = np.mean(med_7)
print(-9999,',',q1,',',q2,',',q3,',',q4,',',q5,',',q6,',',q7,',',9999)
