import numpy as np

shape = (3, 2)
num_arrays = 20

arrays = [np.random.randint(1,20, size = shape) for _ in range(num_arrays)]
arrays = np.array(arrays)
np.save('arrays_file1.npy', arrays)
