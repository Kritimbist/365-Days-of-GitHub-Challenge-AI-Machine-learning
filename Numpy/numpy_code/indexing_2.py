#Ellipsis indexing
import numpy as np

cube = np.random.rand(4,4,4)
print(cube[...,3])

#np.newaxis

import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[:,np.newaxis] )


#modifying array
import numpy as np
arr = np.array([1,2,3,4,5])
arr[1:4]= 11
print(arr)
