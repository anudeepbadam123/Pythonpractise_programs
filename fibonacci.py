#fibonacci 0,1,1,2,3,5,8,13...etc
a,b = 0,1
print(a)
print(b)
for i in range(10):
    sum =a+b
    a=b
    b=sum
    print(sum)
