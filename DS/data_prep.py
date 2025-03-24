# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data=pd.read_excel('dataset/students_mark.xlsx')
print(data['gmarks (Average)'])

plt.hist(data['gmarks (Right)'],
         edgecolor='black', color='red')

#plt.bar(height=data['gmarks (Average)'], x=data['Name'])

mean = data['gmarks (Average)'].mean()

print(data['gmarks (Left)'].var())
print(data['gmarks (Left)'].std())
print(data['gmarks (Left)'].skew())
#plt.show()
