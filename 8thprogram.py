#Create an inner function
# Question description: -
#
# Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
# Create an inner function inside an outer function that will concatenate x and y.
# At last, an outer function will join the word 'developer' to it.
#e/p: EmmaKellyDevelopers

def outer_func(x,y):

    def inner_func(x,y):
        k = x+y
        return k

    a = inner_func(x,y)
    return a+'Developers'


p = outer_func("Emma", "Kelly")
print(p)
