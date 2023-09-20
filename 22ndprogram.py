#Read from one file to to writing into another file

with open("./testread.py","r") as tr:
    a=tr.readlines()
    print(a)
    str1 = "Line5"
    filt_a=[x for x in a if x not in str1]
    print(filt_a)

with open("./testwrite.py", "w+") as tw:
    tw.writelines(filt_a)