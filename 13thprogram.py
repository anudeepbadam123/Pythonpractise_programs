#oddnumbersfrom first list and even numbers from 2nd list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
res_list=[]
for k in list1:
    if k%2!=0:
        res_list.append(k)
for p in list2:
    if p%2==0:
        res_list.append(p)
print(res_list)