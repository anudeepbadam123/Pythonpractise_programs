list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i in range(0, len(list1)):
    k = (len(list2)-1)-i
    print(list1[i], list2[k])