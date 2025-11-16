#accesing array in 1D array
import numpy as np
arr = np.array([10,20,30,40,50,60,70])
print(arr[0]) #gives frist array element -> 10
print(arr[3])#gives fourth  array elememt -> 40
print(arr[-1]) #gives last element of array -> 70


# accessing arrray in 2D
import numpy as np
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(matrix[1,2])#Here matrix[1, 2] accesses the element in the second row (index 1) and third column (index 2) which is 6.
print(matrix[2,1])

#acessing array in 3D
import numpy as np

cube = np.array([[[1,2,3],
                 [4,5,6],
                 [7,8,9]],
                 [[10,11,12],
                  [13,14,15],
                  [16,17,18]]
                 ]
                 )
print(cube[1,2,0])

#Slicing 1D array
import numpy as np
arr = np.array([0,1,2,3,4,5])
print(arr[0:4])

#Slicing multi-dim array
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[0:2, 1:3])
