# data cleaning using pandas
import pandas as pd 
df = pd.read_csv('data.csv')


# df.dropna()
# df.fillna(130,inplace=True)

# print(df)


x=df["Calories"].mean()
print(f"the mean of Calories {x}")


