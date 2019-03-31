import pandas as pd

df = pd.DataFrame({'Date': ['2016-03-01', '2016-03-02', '2016-03-03'],
                   'Type': ['a', 'b', 'c'], 'Value': [11.432, 13.031, 20.234]})

# Rows into columns
df1 = df.pivot(index='Date', columns='Type', values='Value')
df2 = pd.pivot_table(df, index='Date', columns='Type', values='Value')

# Stack/ Unstack
df3 = pd.DataFrame({'0': [0.23, 0.18, 0.43], '1': [0.39, 0.23, 0.43]})
df4 = df3.stack()
df4.unstack()



