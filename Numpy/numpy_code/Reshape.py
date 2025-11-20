import numpy as np
a = np.array([1,2,3,4,5,6])
r = a.reshape(2,3)
print(r)

import numpy as np
a =  np.array([1,2,3,4,5,6,7,8])
r = a.reshape(2,2,2)
print(r)

import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
r = a.reshape(3,-1)
print(r)
