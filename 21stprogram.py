#Exercise 5: Accept a list of 5 float numbers as an input from the user
emp_lst = []
for a in range(1,6):
    # print("Enter float number: ", a)
    a = float(input("Enter"+" " + str(a) + " " + "float number: "))
    emp_lst.append(a)
print(emp_lst)