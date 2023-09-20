#Read text file into a variable and replace all newlines with space
with open("Sampletext3.txt","r") as textfile:
    content = textfile.readlines()

print(content)
content_replaceline = []
for word in content:
    linrep_word =word.replace('\n','')
    content_replaceline.append(linrep_word)
print(" ".join(content_replaceline))