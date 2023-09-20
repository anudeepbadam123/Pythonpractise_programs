sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keyslst = ["name", "salary"]

fin_dict ={}
for k,v in sample_dict.items():
    if k in keyslst:
        fin_dict[k]=v
    else:
        None
print(fin_dict)
