#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:42:37 2019

@author: gurpreet
"""

import numpy as n
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as graph
import os
import csv
import re

path = '/home/gurpreet/Documents/csv_data_subjectwise/S1'
featureList = []
labelsList = []


# Function to read the features from file
# def read_features(par_filename):
#	vl = []
#	with open(par_filename,"r") as file_lines:
#		#features = [[float(i) for i in line.split()] for line in file_lines]
#		for line in file_lines:
#			vl.append(line.split())
#	file_lines.close()
#	for r in vl:
#		del r[12]
#	return vl;
#	
## Function to read the lables from file
# def read_labels(par_filename):
#	vl = []
#	with open(par_filename,"r") as file_lines:
#		for line in file_lines:
#			vl.append(line.split())
#	file_lines.close()
#	ll = []
#	for r in vl:
#		ll.append(r[12])
#	return ll;


def getFeatures():
    for root, dirs, files in os.walk(path):
        for name in files:
            with open(os.path.join(root, name), 'rt') as f:
                count = 0
                # print(name)
                for line in f:
                    a = [float(i) for i in line.split(',')]
                    # print(len(a))
                    featureList.append(a)
                    count = count + 1
                if (re.search("rest", name)):
                    for i in range(count):
                        labelsList.append(0)
                elif (re.search("vowel_a", name)):
                    for i in range(count):
                        labelsList.append(1)
                else:
                    for i in range(count):
                        labelsList.append(0) # a vs rest


# Function to compute the classification using SVM
def compute_SVC(train_f, train_l):
    C = 1.0
    cache_size = 200
    class_weight = None
    coef0 = 0.0
    decision_function_shape = None
    degree = 3
    gamma = 'auto'
    kernel = 'rbf'
    max_iter = -1
    probability = False
    random_state = None
    shrinking = True
    tol = 0.001
    verbose = False
    c = svm.SVC(kernel='linear', C=100)
    c.fit(train_f, train_l)
    return c


# Function to calculate the accuracy
def compute_accuracy(test_f, test_l, c):
    pred = c.predict(test_f)
    print(pred)
    pred_accu = accuracy_score(test_l, pred)
    return pred_accu


# Function to compute the confusion matrix
def compute_confusion_matrix(test_f, test_l, c):
    pred = c.predict(test_f)
    x = confusion_matrix(test_l, pred)
    return x


# Starting of the flow of program
getFeatures()
# read_data_features_train = read_features("plrx.txt");
# read_data_labels_train = read_labels("plrx.txt");
model_svc = compute_SVC(featureList, labelsList)
accu_percent = compute_accuracy(featureList, labelsList, model_svc) * 100;
print("Accuracy obtained over the whole training set is %0.6f %% ." % (accu_percent))
# conf_mat = compute_confusion_matrix(read_data_features_train,read_data_labels_train,model_svc);
# print conf_mat
