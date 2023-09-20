#Filter dictionary to contain keys present in the given list
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# Filter dict using following keys
l1 = ['A', 'C', 'F']
desired_dict = {}
for k,v in d1.items():
    if k in l1:
        desired_dict[k] = v
    else:
        None
print(desired_dict)
