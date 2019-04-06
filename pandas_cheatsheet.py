import pandas as pd
import numpy as np
from sklearn.utils import shuffle

df = pd.DataFrame({'Date': ['2016-03-01', '2016-03-02', '2016-03-03'],
                   'Type': ['a', 'b', 'c'], 'Value': [11.432, 13.031, 20.234]})

# Rows into columns
df1 = df.pivot(index='Date', columns='Type', values='Value')
df2 = pd.pivot_table(df, index='Date', columns='Type', values='Value')

# Stack/ Unstack
df3 = pd.DataFrame({'0': [0.23, 0.18, 0.43], '1': [0.39, 0.23, 0.43]})
df4 = df3.stack()
df4.unstack()

pd.melt(df, id_vars=['Date'], value_vars=["Type", "Value"], value_name="Obsevations")

# Iterations
df.iteritems()
df.iterrows()

## Indexing

# Selecting
df3 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [12, 5, 6, 9, 2]})
df3.loc[:, (df3 < 7).any()] # any col
df3.loc[:, (df3 > 3).all()] # ALL col

df4 = df3[df3 > 8]
df4.loc[:, df4.isnull().any()]
df4.loc[:, df4.notnull().any()]

# isin
df4 = df4.fillna(np.random.random())
df3['A'][df3['A'].isin([1, 2, 3])]
df3.filter(items=["A", "B"])
df3.where(df3 >= 8)
df3.query('C<B')

# Setting Index
df3 = shuffle(df3)
df3 = df3.reset_index()
df3 = df3.rename(index=str, columns={"A": "ONE", "B": "TWO","C": "THREE"})








