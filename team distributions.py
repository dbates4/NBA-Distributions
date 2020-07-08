# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:45:14 2020

@author: dylan
"""

import pandas as pd

datapath = "C:/Users/dylan/Datasets/NBA/box scores 2016 to 2017.csv"

df = pd.read_csv(datapath)

df = df.drop(columns=['Unnamed: 0'])

df_teamlevel = df.groupby(['Team','Date'])

# just trying out a thing

