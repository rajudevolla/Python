# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
mat1=np.zeros((4,4),dtype=int)
print(mat1)


#Negate all values which are more than 5 in a row
arr1=np.arange(11)
arr1[arr1>5]=-arr1[arr1>5]


arr1[6:]=-arr1[6:]    

mat1 = np.array([['abc','A'],['def','B'],['ghi','C'],['jkl','D']])
arr = np.array(['abc','dfe','ghi','kjl']) 

 #sorty array by second column. 
arr = np.array([[1,21,3],[5,4,2],[56,12,4]])
print(arr[arr[:,1].argsort()])
#Get top 4 values in array
arr = np.array([90, 14, 24, 13, 13, 590, 0, 45, 16, 50])
print(arr[np.argpartition(arr,-4)[-4:]])
 
#Find the nearest number from the given number in an array.
arr = np.array([10,55,22,3,6,44,9,54])
nearest_to = 50
print( arr[np.abs(arr-nearest_to).argmin()])

mat = np.array([[10,5,9],
                [2,20,6],
                [8,3,30]]).reshape(3,3)

#N1 to the upper half elements of mat, find highest number


#N2 to the main diagonal elements of mat, find highest number


#N3 to the lower half elements of mat, find highest number






