"""
The target of this exercise is to create two lists called x_list and y_list,
which contain 10 instances of the variables x and y, respectively.
You are also required to create a list called big_list,
which contains the variables x and y, 10 times each,
by concatenating the two lists you have created.
"""
x=1
y=2
x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list
print(big_list)