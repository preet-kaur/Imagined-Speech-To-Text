import scipy.io
import numpy as np

data = scipy.io.loadmat("sub_4b_ch80_v_eog_removed_256Hz.mat")

for i in data:
	if '__' not in i and 'readme' not in i:
		np.savetxt((i+".csv"),data[i],fmt='%s',delimiter=',')