#Remove first n characters from a string

def remove_nstr(input_str, remove_number_chars):
    new_str = ''
    for ch in range(0,len(input_str)):
        if ch>=remove_number_chars-1:
            new_str = new_str+input_str[ch]
        else:
            None
    return new_str

b= remove_nstr("Anudeep",4)
print(b)