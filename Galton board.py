import numpy as np
from numpy.core.defchararray import lower

def diffuse(array):
    array1=np.zeros(len(array))
    for x in range(len(array)):
        if x==0 or x==len(array)-1:
            continue
        if array[x]!=0:
            a=array[x]
            array1[x-1]=array1[x-1]+a/2
            array1[x+1]=array1[x+1]+a/2
    return array1

def sum_in_range(array,lower_bond,upper_bond):
    value=0
    for x in range(upper_bond-lower_bond):
        index=x+lower_bond
        value+=array[index]
    return value

layers=1000
array=np.zeros(layers)
array[int(layers/2)]=1
for _ in range(layers):
    array=diffuse(array)
print(sum_in_range(array,400,600))

##failed