import numpy as np
a = np.array((1, 2))
b = np.array((4, 5))

dist = np.linalg.norm(a-b)

print(dist)