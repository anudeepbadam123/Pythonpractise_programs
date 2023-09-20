# In this question, You need to remove items from a list while iterating but without creating a different copy of a list.
# Remove numbers greater than 50
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def filter_list(x):
    if x<=50:
        return True
    else:
        return False


number_list = list(filter(filter_list, number_list))
print(number_list)

