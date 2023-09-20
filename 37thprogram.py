import pandas as pd
df1 =pd.read_csv("data1.csv")
df2 =pd.read_csv("data2.csv")
res = df1.equals(df2)
print(res)
if res != True:
    print("df1 and df2 are not similar")
    difference = df1.compare(df2)
    # print(difference)
    # mask = (df1 != df2).any(axis=1)
    #
    # # Filter rows with differences
    # differences = df1[mask]
    # print(differences)
    difference.to_csv("data3diff.csv", index= False)
merged_df = pd.merge(df1, df2, how='inner', on=['dial_code','country'], left_on=None, right_on=None, left_index=False, right_index=False, suffixes=('_left', '_right'), sort=True)
print(merged_df.head(2))


# print(df)