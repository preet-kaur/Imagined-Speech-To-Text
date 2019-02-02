"""

This file contains python code to load mat file.
Each .mat file contains eeg data of one subject.
There are 2 variables:
    1) eeg_data_wrt_task_rep_no_eog_256Hz_end_trial
    2) eeg_data_wrt_task_rep_no_eog_256Hz_last_beep

Each variable contains 3 rows for 3 vowels and 100 columns for 100 trials
Each cell (for every row and every column) contains array, dimension: 80x512

"""

from scipy.io import loadmat
import pandas as pd

mat = loadmat('sub_4b_ch80_v_eog_removed_256Hz.mat')

mdata = mat['eeg_data_wrt_task_rep_no_eog_256Hz_end_trial']
df = pd.DataFrame(mdata)
vowel_a_00 = df.iloc[0][0]  #vowel 'a', trial 1
vowel_a_00_channels_df = pd.DataFrame(vowel_a_00)

vowel_a1 = df.iloc[0]       #vowel 'a', 100 trials
vowel_a_df = pd.DataFrame(vowel_a1)


"""
Reference:  https://www.kaggle.com/avilesmarcel/open-mat-in-python-pandas-dataframe


from scipy.io import loadmat
import pandas as pd

mat = loadmat('../input/train_1/1_1_0.mat')

mdata = mat['dataStruct']

mtype = mdata.dtype

ndata = {n: mdata[n][0,0] for n in mtype.names}

ndata

data_headline = ndata['channelIndices']
print(data_headline)

data_headline = data_headline[0]

data_raw = ndata['data']
len(data_raw)

pdata = pd.DataFrame(data_raw,columns=data_headline)

pdata

"""