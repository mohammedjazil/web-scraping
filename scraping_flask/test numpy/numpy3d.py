import numpy as np 
tda=np.array([[[1,2,3],
              [4,5,6]],
             
              [[7,8,9],
              [10,11,12]]])

print(tda[0,1,2])
print(tda.shape)

print(np.sort(tda))

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

newarr = np.concatenate((arr1,arr2))
print("concatented array :",newarr)


