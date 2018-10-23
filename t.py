# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iniciar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4

import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import numpy as np
import peakutils

mat = scipy.io.loadmat('18.mat')
for i in mat:
	if '__' not in i and 'readme' not in i:
		np.savetxt(("files.csv"),mat['ppg_inv'],delimiter=',')
#cb = np.array(mat[5_ppginv])

#indexes = peakutils.indexes(cb,thres=0.02/max(cb),min_dist=100)


'''mat = scipy.io.loadmat('5.mat')
cardio_df = pd.DataFrame(np.hstack((mat['x'], mat['y'])))
cardio_df.head()
cardio_df.shape'''

'''d = {'5.mat'}
df = pd.DataFrame(data=d)

print (df)'''

print(mat)