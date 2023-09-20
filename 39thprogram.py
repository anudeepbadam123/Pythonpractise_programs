# Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res_lst=[]
for i in range(0, len(list1)):
    wr = list1[i] + list2[i]
    res_lst.append(wr)

print(res_lst)