import numpy as np
import matplotlib.pyplot as plt
import sys

d = np.load(sys.argv[1])
plt.figure()
plt.imshow(d)
plt.show()
