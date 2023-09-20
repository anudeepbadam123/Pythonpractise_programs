#Reverse Dictionary mapping
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
desired_dict = {}
for k in ascii_dict.items():
    print(k[1], k[0])
    desired_dict.update(k[1])
    # desired_dict.updat