#Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
sam_lst=[]
dup_lst =[]
for k in sample_list:
    if k not in sam_lst:
        sam_lst.append(k)
    else:
        dup_lst.append(k)
print(dup_lst)