import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9])
# print("array is",arr)
# print(type(arr))
print(arr[3]+arr[4])
print(arr[:4])
print(arr[4:])
print(arr[1:5:2])
print(arr[1::2])


x=np.where(arr==4)
print(x)