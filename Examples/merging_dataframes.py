import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from molSimplify.Classes.mol3D import mol3D

plt.rc('font',size=15)


df = pd.merge(df_5,df_10,how='outer',on='refcode')
df = pd.merge(df,df_12_5,how='outer',on='refcode')
df = pd.merge(df,df_15,how='outer',on='refcode')
df = pd.merge(df,df_17_5,how='outer',on='refcode')
df = pd.merge(df,df_20,how='outer',on='refcode')
df = pd.merge(df,df_20nd,how='outer',on='refcode')
df = pd.merge(df,df_15t,how='outer',on='refcode')
df = pd.merge(df,df_15vvt,how='outer',on='refcode')


df1 = pd.read_csv('round1_e_finished.csv')
df2 = pd.read_csv('round1_scre_finished.csv')
df = pd.concat([df1,df2],axis=0)
#Combine DataFrame objects with overlapping columns and return everything. Columns outside the intersection will be filled with NaN values
