#1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
row_num =5

for i in range(1,row_num+1):
    for j in range(1, i+1):
        print(j, end= " ")

    print("")