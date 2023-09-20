import pandas as pd
data1 = {"country":["India","USA","UK","Germany"],"dial_code":[91,1,44,49]}
df1 = pd.DataFrame(data1)
df1.to_csv("data1.csv",index= None)
df1 = pd.read_csv("data1.csv")
# print(dir(df1))
itr = dir(df1)
for i in itr:
    print(i)
# df2 = pd.read_csv("data2.csv")