import pandas as pd
import quandl

#Load in dataet from quandal into a dataframe df
df = quandl.get('WIKI/GOOGL')

#print the head of the dataframe

print(df.head())

# Select only the required features

df = df [['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Add column PCT_change, HL_PCT

df['HL_PCT'] = ((df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']) * 100
df['PCT_change'] = ((df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']) * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

# Adjuste df

print("\n\n\n Adjusted Dataframe \n")
print(df.head())