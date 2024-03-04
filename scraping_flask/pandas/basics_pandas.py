import pandas as pd 

# data = {
#     "calories":[420,380,390],
#     "durations":[50,40,45]
# }

# df=pd.DataFrame(data) #converting to dataframe

# print(df)
# print(df.loc[0]) #converting to 0th index

# # named index

# df= pd.DataFrame(data,index=["day1","day2","day3",])

# print(df)

# print(df.loc["day2"]) #retriving data of day2

df =pd.read_csv("data.csv")
print(df)

print(df.head(10))