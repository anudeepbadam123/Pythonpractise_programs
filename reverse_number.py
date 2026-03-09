#integer to reverse and display a string

str1=""
k =7536
while k>0:
    str1 = (k%10)
    k = (k//10)
    print(str(str1), sep='', end=' ')
