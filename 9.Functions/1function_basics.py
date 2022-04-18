"""
Functions are a convenient way to divide your code into useful blocks, 
allowing us to order our code, 
make it more readable, 
reuse it and save some time.
"""

# Defining a function
from re import A


def myFunc():
    print('I am awesome')


# calling it later
myFunc()

# Function with variables
def myGreet(user_name,age):
    print('Hi %s you are awesome @ %d'%(user_name, age))

myGreet("Ramarao", 34)

#The 'return' keyword is used to return a value to the caller.
def simple_add(a,b):
    return a+b
simple_add(5,6)