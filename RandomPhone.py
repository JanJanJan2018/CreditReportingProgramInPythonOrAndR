import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#========================================================


# Create a phone number to attach or append to the area code field

phone = np.random.rand(100,1)
print(phone)
phone = phone*(10**7)
print(phone)
print(type(phone)) #numpy.ndarray
print(min(phone),max(phone)) #[118684.10728358] [9958124.17135941]

Rphone = []
for i in phone:
    i=int(i)
    if (i < 1000000) & (i > 100000):
        i = i*(10**1)
    elif (i < 1000000) & (i > 10000):
        i = i*(10**(2))
    elif (i > 9999999):
        i = i*(10**(-1))
    else:
        i = i
    Rphone.append(i)
print(Rphone)
print(min(Rphone), max(Rphone)) # 1018302 9957560

PhoneNumber = pd.Series(Rphone)
PhoneNum = PhoneNumber.T

Phone = pd.DataFrame(PhoneNum)
Phone.columns = ["PhoneNumber"]

print(Phone)
#  PhoneNumber
# 0       6435636
# 1       5337185
# 2       4363513
# 3       2813840
# ...
# 97      4948277
# 98      1182710
# 99      6152229
#
# [100 rows x 1 columns]
#

import os
path="c:/Users/jlcor/Downloads"
os.chdir(path)

os.getcwd()

Phone.to_csv("phoneGenerator7digits.csv")



