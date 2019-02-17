#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:27:20 2019

@author: gurpreet
"""

import os
import h5py
import re
import numpy
import pandas as pd

S1_train_rest = []
S1_train_vowel_a = []
S1_train_vowel_u = []

S2_train_rest = []
S2_train_vowel_a = []
S2_train_vowel_u = []

S3_train_rest = []
S3_train_vowel_a = []
S3_train_vowel_u = []

S1_test_rest = []
S1_test_vowel_a = []
S1_test_vowel_u = []

S2_test_rest = []
S2_test_vowel_a = []
S2_test_vowel_u = []

S3_test_rest = []
S3_test_vowel_a = []
S3_test_vowel_u = []

file_va = []

path = "/home/gurpreet/Documents/BE Project/datasets/Speech Imagery Dataset/prj/data/SupplementaryFiles"
csv_file_path = "/home/gurpreet/Documents/csv_data_subjectwise"


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


def create_csv(name, new_filename):
    for filename in name:
        full_path = path + "/" + filename
        f = h5py.File(full_path)
        data = numpy.array(f['filteredEEG']['data'])
        subject_csv_file_path = csv_file_path + '/' + new_filename[:2]
        if not os.path.exists(subject_csv_file_path):
            os.mkdir(subject_csv_file_path)
        with open(subject_csv_file_path + '/' + new_filename + '.csv', 'ab') as f_handle:
            numpy.savetxt(f_handle, data, delimiter=",")


for file in files(path):
    file_va.append(file)
    file_va.sort()
    full_path = path + "/" + file
    f = h5py.File(full_path)

    flag = 999

    if (re.search("train", file)):
        if (f['labels']['data'].value[0] == 0.):
            flag = 0
        elif (f['labels']['data'].value[0] == 1.):
            flag = 1
        elif (f['labels']['data'].value[0] == 2.):
            flag = 2

        if (re.findall("\AS1", file)):
            if(flag == 0):
                S1_train_rest.append(file)
                S1_train_rest.sort()
            elif (flag == 1):
                S1_train_vowel_a.append(file)
                S1_train_vowel_a.sort()
            elif (flag == 2):
                S1_train_vowel_u.append(file)
                S1_train_vowel_u.sort()
        elif (re.findall("\AS2", file)):
            if(flag == 0):
                S2_train_rest.append(file)
                S2_train_rest.sort()
            elif (flag == 1):
                S2_train_vowel_a.append(file)
                S2_train_vowel_a.sort()
            elif (flag == 2):
                S2_train_vowel_u.append(file)
                S2_train_vowel_u.sort()
        elif (re.findall("\AS3", file)):
            if(flag == 0):
                S3_train_rest.append(file)
                S3_train_rest.sort()
            elif (flag == 1):
                S3_train_vowel_a.append(file)
                S3_train_vowel_a.sort()
            elif (flag == 2):
                S3_train_vowel_u.append(file)
                S3_train_vowel_u.sort()


    elif (re.search("test", file)):
        if (f['labels']['data'].value[0] == 0.):
            flag = 0
        elif (f['labels']['data'].value[0] == 1.):
            flag = 1
        elif (f['labels']['data'].value[0] == 2.):
            flag = 2

        if (re.findall("\AS1", file)):
            if (flag == 0):
                S1_test_rest.append(file)
                S1_test_rest.sort()
            elif (flag == 1):
                S1_test_vowel_a.append(file)
                S1_test_vowel_a.sort()
            elif (flag == 2):
                S1_test_vowel_u.append(file)
                S1_test_vowel_u.sort()
        elif (re.findall("\AS2", file)):
            if (flag == 0):
                S2_test_rest.append(file)
                S2_test_rest.sort()
            elif (flag == 1):
                S2_test_vowel_a.append(file)
                S2_test_vowel_a.sort()
            elif (flag == 2):
                S2_test_vowel_u.append(file)
                S2_test_vowel_u.sort()
        elif (re.findall("\AS3", file)):
            if (flag == 0):
                S3_test_rest.append(file)
                S3_test_rest.sort()
            elif (flag == 1):
                S3_test_vowel_a.append(file)
                S3_test_vowel_a.sort()
            elif (flag == 2):
                S3_test_vowel_u.append(file)
                S3_test_vowel_u.sort()

# Rest (0)
# a (1)
# u (2)

create_csv(S1_train_rest, "S1_train_rest")
create_csv(S1_train_vowel_a, "S1_train_vowel_a")
create_csv(S1_train_vowel_u, "S1_train_vowel_u")

create_csv(S2_train_rest, "S2_train_rest")
create_csv(S2_train_vowel_a, "S2_train_vowel_a")
create_csv(S2_train_vowel_u, "S2_train_vowel_u")

create_csv(S3_train_rest, "S3_train_rest")
create_csv(S3_train_vowel_a, "S3_train_vowel_a")
create_csv(S3_train_vowel_u, "S3_train_vowel_u")


create_csv(S1_test_rest, "S1_test_rest")
create_csv(S1_test_vowel_a, "S1_test_vowel_a")
create_csv(S1_test_vowel_u, "S1_test_vowel_u")

create_csv(S2_test_rest, "S2_test_rest")
create_csv(S2_test_vowel_a, "S2_test_vowel_a")
create_csv(S2_test_vowel_u, "S2_test_vowel_u")

create_csv(S3_test_rest, "S3_test_rest")
create_csv(S3_test_vowel_a, "S3_test_vowel_a")
create_csv(S3_test_vowel_u, "S3_test_vowel_u")