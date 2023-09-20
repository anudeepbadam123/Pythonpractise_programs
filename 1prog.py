#Reverse each word of a string

def str_rev(str_word):
    rev_str=""
    for a in str_word:
        rev_str = a+rev_str
    return rev_str

str_phrase ="My name is Anudeep"
rev_Str_phrase=[]
lst_strphrase = list(str_phrase.split(" "))
rev_lst_words = lst_strphrase[::-1]
print(rev_lst_words)
for p in rev_lst_words:
    a = str_rev(p)
    rev_Str_phrase.append(a)
    # rev_Str_phrase.append(" ")
print(" ".join(rev_Str_phrase))