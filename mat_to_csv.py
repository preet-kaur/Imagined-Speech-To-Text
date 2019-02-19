#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:16:46 2019

@author: gurpreet
"""

import os
import numpy
import pandas as pd
from scipy.io import loadmat
import csv

file_va = []
files_old_csv = []

path = '/home/gurpreet/Documents/BE Project/datasets/imagined speech/Vowels'
csv_file_path = '/home/gurpreet/Documents/imagined_speech_csv/vowels'


def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file



def create_csv(filename):
    full_path = path+"/"+filename
    mat = loadmat(full_path)
    mdata = mat['eeg_data_wrt_task_rep_no_eog_256Hz_last_beep']
    df = pd.DataFrame(mdata)
    
    for kk in range(len(df)):   # here, len(df) = 3, since a,i,u
        vowel_a = df.iloc[kk]               # vowel a/i/u 100 trials
        vowel_a_df = pd.DataFrame(vowel_a)  # (100x1)
        
        if kk == 0:         # vowel a
            flag = '__A'
        elif kk == 1:       # vowel i
            flag = '__I'
        elif kk == 2:
            flag = '__U'    # vowel u
        
        print(flag)
        new_filename = filename+flag
        
        for jj in range(len(vowel_a_df)):
            vowel_a_trial = vowel_a_df.iloc[jj][kk]
            data = numpy.array(vowel_a_trial)   # shape = 64x1280 OR 80x1280
            data = data.transpose()             # shape = 1280x64 OR 1280x80
            with open(csv_file_path+'/'+new_filename+'.csv','a') as f_handle:
                numpy.savetxt(f_handle, data, delimiter=",")
                

def interchange_rows_col(old_filename, new_filename):
    a = zip(*csv.reader(open(csv_file_path+'/'+old_filename, 'rt')))
    csv.writer(open(csv_file_path+'/'+new_filename+'.csv', 'wt')).writerows(a)
                
for file in files(path): 
    file_va.append(file)
    file_va.sort()               
  
for filename in file_va:
    create_csv(filename)
  
    
# interchange rows n columns
for file in files(csv_file_path):
    files_old_csv.append(file)
    files_old_csv.sort()
    
for filename in files_old_csv:
    new_filename = filename+'__new'
    interchange_rows_col(filename, new_filename)

    