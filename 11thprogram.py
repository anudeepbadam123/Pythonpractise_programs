#str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
str1 = "pynative"
counter_n = 0
for a in range(0,len(str1)):
    if(counter_n %2 ==0):
        print(str1[counter_n])
    counter_n = counter_n + 1