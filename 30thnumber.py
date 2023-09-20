#Count the total number of digits in a number
numbers = 421412
count = 0
while numbers>0:
    k = numbers%10
    numbers = numbers//10
    count=count+1
print(count)