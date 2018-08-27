import numpy as np
import pandas as pd
from pandas import Series, DataFrame


#============================================================================
#warming up, with left and right justify for column formatting later

# g = ['t','r','w']
# type(g)
# print(g)
# print(type(g))
# # ['t', 'r', 'w']
# # <class 'list'>
#
#
# gg = 'tWrr'
# G = gg.upper()
# print(G)
# #TWRR
#
#
#
# h = input("what time is it? ")
#
# print("Today at",h,"it is cold.")
#
# H = "Today at " +h+" it is cold"
# H = H.ljust(30,'*')
# print(H)
# # what time is it?7 am
# # Today at 7 am it is cold.
# # Today at 7 am it is cold******
# k = "Tomorrow at "+h+" it will be warm. "
# K = k.rjust(60,'=')
# print(K)
# #==========================Tomorrow at 7 am it will be warm.
#================================================================================


#program to generate 100 random SSNs and 100 random Regular Scheduled Payments

a = np.random.rand(100,1)
ab = a*(10**9)

print(ab)

SSN = ab
print(SSN)
print(type(SSN)) #numpy.ndarray is the class
print(min(SSN),max(SSN)) #[167484.26803803] [9.98328663e+08]

Social = []
for i in SSN:
    i = int(i)
    if (i < 100000000) & (i > 10000000):
        i = i*(10**1)
    elif (i < 100000000) & (i > 1000000):
        i = i*(10**2)
    elif (i < 100000000) & (i > 100000):
        i = i*(10**3)
    elif i > 999999999:
        i = i*(10**(-1))
    else:
        i=i
    Social.append(i)
print(min(Social),max(Social)) #107212273 982183944

print(Social)
print(type(Social)) #list

social = pd.Series(Social)
print(type(social))#pandas.core.series.Series
print(social)

regPMT = np.random.rand(100,1)
PMT = regPMT*(10**3)

print(type(PMT))#numpy.ndarray

PMT2 = []
for i in PMT:
    i = int(i)
    if i < 20:
        i = i*(10**2)
    elif i < 100:
        i = i+100
    else:
        i = i
    PMT2.append(i)
print(PMT2)
print(type(PMT2))#list

RegPmt = pd.Series(PMT2)
print(RegPmt)
print(type(RegPmt))#pandas.core.series.Series


#Put the series together for SSN and RegPmt into a data frame
SSNandPMT = pd.DataFrame([social,RegPmt])
SSNandPMT2 = SSNandPMT.T
print(SSNandPMT2)
#             0    1
# 0   316618114  999
# 1   228321807  982
# 2   684216868  194
# 3   382000819  491
# ...
# 97  222885077  185
# 98  293207191  165
# 99  300100656  733

#Give the data frame columns corresponding header names
SSNandPMT2.columns=["Social","RegPMT"]
print(SSNandPMT2)
#        Social  RegPMT
# 0   880261788     827
# 1   208196300     840
# 2   573881700     478
# 3   788512135     883
# ...
# 98  585996715     113
# 99  107955619     735
#
# [100 rows x 2 columns]



#To save this table to csv in downloads directory
import os
path="c:/Users/jlcor/Downloads"
os.chdir(path)

os.getcwd()

SSNandPMT2.to_csv("SSN_PMT.csv")

SSNandPMT2.close()

