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

print(type(data))

print(data['Close'])

print(type(data['Close']))

daily_chg = data['Close'] - data['Open']

print(type(daily_chg))

daily_pct_chg = ((data['Close'] - data['Open'])/data['Open'])*100

print(daily_pct_chg)

print(data['Close'].iloc[0],data['Close'].iloc[-1])

norm = data['Close']/data['Close'].iloc[0]

print(norm)

data['Daily chg'] = data['Close'] - data['Open']

print(data.head())

data['Normalized'] = data['Close']/data['Close'].iloc[0]

print(data.head())

print(data.tail())

print(data['Close'].min())

print(data.min())

print(data['Close'].argmin())

print(data.iloc[33:40])

print(data['Normalized'].min())

print(data['Normalized'].argmin())

print(data['Close'].max())

print(data['Close'].argmax())

print(data.iloc[251:])

print(data['Close'].mean())

print(data.drop(labels=['High', 'Low', 'Adj Close', 'Volume'], axis = 1, inplace=True))

print(data.head())








