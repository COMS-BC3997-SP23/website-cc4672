# -*- coding: utf-8 -*-
"""Apple_Balance_Sheet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gOKxd6wauDoP7ZgwM7btwSMRW9DzYOPK
"""

import pandas as pd
import numpy as np

try:
    df = pd.read_excel("/content/Apple_10K_2022.xlsx")
except FileNotFoundError:
    print("Error,please re-try")

df

df_balance= pd.read_excel('/content/Apple_10K_2022.xlsx', sheet_name='BALANCE_SHEET')
df_balance.head(20)

df_balance.columns

new_balance = df_balance.drop('Created by EDGAR Online, Inc.', axis=1)
new_balance = new_balance.iloc[16:, :]
new_balance

new_balance=new_balance.fillna('')

new_balance=new_balance.rename(columns={'Unnamed: 1': ' ', 'Unnamed: 2': '2022', 'Unnamed: 3': '2021'})

new_balance

"""Unlike working in excel, with python, I need to first do clean-up of the null values (null rows). I also need to reset the indexes. Hence, creating more work"""

new_balance.info()

new_balance2 = new_balance.reset_index(drop=True)
new_balance2

cash=new_balance2.iloc[2]
current_receivables=new_balance2.iloc[7]
current_liabilities=new_balance2.iloc[24]

quick_ratio=int(cash+current_receivables)/current_liabilities

quick_ratios = []

for index, row in new_balance2.iterrows():
    cash = row['Cash and cash equivalents']
    current_receivables = row['Accounts receivable, net']
    current_liabilities = row['Total current liabilities']
    quick_ratio = (cash + current_receivables) / current_liabilities
    quick_ratios.append(quick_ratio)
    
print(quick_ratios)

quick_ratios = []

for index, row in new_balance2.iterrows():
    cash = row[2]
    current_receivables = row[7]
    current_liabilities = row[24]
    quick_ratio = (cash + current_receivables) / current_liabilities
    quick_ratios.append(quick_ratio)
    
print(quick_ratios)

#new_balance2.set_index(' ',inplace=True)
new_balance2

# Create dataframe for 2021
df_2021 = pd.DataFrame(new_balance2.loc['ASSETS:':"Total liabilities and shareholders' equity", '2021']).transpose()

# Rename columns to remove the extra whitespace
df_2021.columns = df_2021.columns.str.strip()

# Calculate quick ratio for 2021
quick_ratio_2021 = (df_2021['Cash and cash equivalents'] + df_2021['Accounts receivable, net']) / df_2021['Total current liabilities']

# Create dataframe for 2022
df_2022 = pd.DataFrame(new_balance2.loc['ASSETS:':"Total liabilities and shareholders' equity", '2022']).transpose()

# Rename columns to remove the extra whitespace
df_2022.columns = df_2022.columns.str.strip()

# Calculate quick ratio for 2022
quick_ratio_2022 = (df_2022['Cash and cash equivalents'] + df_2022['Accounts receivable, net']) / df_2022['Total current liabilities']

# Print results
print("Quick ratio for 2021:", quick_ratio_2021)
print("Quick ratio for 2022:", quick_ratio_2022)

current_ratio_2021=df_2021['Total current assets']/df_2021['Total current liabilities']
current_ratio_2022=df_2022['Total current assets']/df_2022['Total current liabilities']

print(current_ratio_2021,"\n")
print(current_ratio_2022)





