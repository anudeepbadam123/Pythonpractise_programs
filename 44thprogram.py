#Add new item to list after a specified item
#Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2][2]=7000
# print(list1)
list1.insert(3, 7000)
print(list1)