#squareof numbers
numbers = [1, 2, 3, 4, 5, 6, 7]


def sqr(i):
    return i*i


sqr_numbers = list(map(sqr, numbers))
print(sqr_numbers)