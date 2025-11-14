import numpy as np

random_array = np.random.rand(3,3) #filled with random values sampled from uniform distribution
normal_array = np.random.randn(3,3) # filled with random values sampled from standard normal distribution
randint_array = np.random.randint(1,10,size=(3,3)) # filled with random integers within a given range

print(random_array)
print(normal_array)
print(randint_array)
