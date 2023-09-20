#Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for k,v in sample_dict.items():
    if k in keys:
        sample_dict.pop(k)

print(sample_dict)