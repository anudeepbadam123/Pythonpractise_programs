#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res_lst =[]
for i in range(len(list1)):
    for k in range(len(list2)):
        a = list1[i]+list2[k]
        res_lst.append(a)

print(res_lst)