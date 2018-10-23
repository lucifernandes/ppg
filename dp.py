
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
x = electrocardiogram()
peaks, _ = find_peaks(x, distance=1000)
np.diff(peaks)
#array([186, 180, 177, 171, 177, 169, 167, 164, 158, 162, 172])
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.show()