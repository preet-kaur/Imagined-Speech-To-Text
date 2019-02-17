#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 19:49:02 2019

@author: gurpreet
"""

# Labels description: '0 = re, 1 = ai, 2 = ui'

import os
import h5py
import re 
import numpy
import pandas as pd
import csv

train_rest = []
train_vowel_a = []
train_vowel_u = []

test_rest = []
test_vowel_a = []
test_vowel_u = []

file_va = []

path = "/home/gurpreet/Documents/BE Project/datasets/Speech Imagery Dataset/prj/data/SupplementaryFiles"
csv_file_path = "/home/gurpreet/Documents/csv_data"


def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
            
def create_csv(name, new_filename):
    for filename in name:
        full_path = path+"/"+filename
        f = h5py.File(full_path)
        data = numpy.array(f['filteredEEG']['data'])
        with open(csv_file_path+'/'+new_filename+'.csv','a') as f_handle:
            numpy.savetxt(f_handle, data, delimiter=",")
            
def interchange_rows_col(old_filename, new_filename):
    a = zip(*csv.reader(open(csv_file_path+'/'+old_filename+'.csv', 'rt')))
    csv.writer(open(csv_file_path+'/'+new_filename+'.csv', 'wt')).writerows(a)



            


for file in files(path):  
    file_va.append(file)
    file_va.sort()
    full_path = path+"/"+file
    f = h5py.File(full_path)
    
    if(re.search("train", file)):
        if(f['labels']['data'].value[0] == 0.):
            train_rest.append(file)
            train_rest.sort()
        elif(f['labels']['data'].value[0] == 1.):
            train_vowel_a.append(file)
            train_vowel_a.sort()
        elif(f['labels']['data'].value[0] == 2.):
            train_vowel_u.append(file)
            train_vowel_u.sort()
    
    elif(re.search("test", file)):
        if(f['labels']['data'].value[0] == 0.):
            test_rest.append(file)
            test_rest.sort()
        elif(f['labels']['data'].value[0] == 1.):
            test_vowel_a.append(file)
            test_vowel_a.sort()
        elif(f['labels']['data'].value[0] == 2.):
            test_vowel_u.append(file)
            test_vowel_u.sort()     

# Rest (0)
create_csv(train_rest, "train_rest")
create_csv(train_vowel_a, "train_vowel_a")

# a (1)
create_csv(train_vowel_u, "train_vowel_u")
create_csv(test_rest, "test_rest")

# u (2)
create_csv(test_vowel_a, "test_vowel_a")
create_csv(test_vowel_u, "test_vowel_u")


# interchanging rows and columns in csv files
interchange_rows_col("train_rest", "train_rest_new")
interchange_rows_col("train_vowel_a", "train_vowel_a_new")
interchange_rows_col("train_vowel_u", "train_vowel_u_new")
interchange_rows_col("test_rest", "test_rest_new")
interchange_rows_col("test_vowel_a", "test_vowel_a_new")
interchange_rows_col("test_vowel_u", "test_vowel_u_new")
