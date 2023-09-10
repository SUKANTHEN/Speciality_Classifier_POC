"""
Data Conversion
"""
import pandas as pd

data = pd.read_csv('db/data.dat', delimiter='\t', header=None)

data.columns = ['Class', 'Notes']
data.to_excel('db/data.xlsx', index=False)
