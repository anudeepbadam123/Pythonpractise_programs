#Exercise 3: Calculate the sum of all numbers from 1 to a given number
given_number = 10
sum =0
for i in range(0, given_number):
    k = int(input(f"Enter {i} number: "))
    sum=sum+k

print(sum)