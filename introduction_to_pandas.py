import pandas as pd
data = pd.read_csv("AAPL.csv",index_col=0, parse_dates=True)
print(data.head())
print(data.dtypes)
print(data.index)
print(data.loc["2020-01-27"])

print(data.loc["2021-01-01":])

print(data.loc["2020-06-01":"2020-07-01"])

print(data.loc[:"2020-07-01"])

print(data.iloc[0])

print(data.iloc[-1])