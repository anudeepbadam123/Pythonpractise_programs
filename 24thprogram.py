#to echeck file empty or not

with open("testwrite.py", "r") as tw:
    tr= tw.readlines()
    if len(tr)>0:
        print("File contains Content")
    else:
        print("File is empty")