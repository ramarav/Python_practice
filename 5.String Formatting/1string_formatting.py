"""
Let's say you have a variable called "name" with your user name in it,
and you would then like to print(out a greeting to that user.)
"""
name = 'ramarao'
print('Hello Mr.%s'%name)
"""
To use two or more argument specifiers, use a tuple (parentheses):
"""
age = 30
print('Hello Mr.%s. You are %d years old'%(name,age))
"""
Any object which is not a string can be formatted using the %s operator as well. 
The string which returns from the "repr" method of that object is formatted as the string.
"""
myList = [1,2,3]
print('The list is : %s'%myList)
"""
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
"""
