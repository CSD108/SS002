import numpy as np
import matplotlib.pyplot as plt

with open ("11072024-bitstream.txt","r") as file:
    st = [line for line in file][0]
max_length = len(st)
print(max_length)
index = 0
dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
while index<max_length:
    dict[int(st[index:index+3],2)]+=1
    index+=3
print(dict)