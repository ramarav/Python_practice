"""
The __init__() function, is a special function that is called when the class is being initiated.
It's used for asigning values in a class.
"""


class NumberHolder:

    def __init__(self, number):
        self.number = number*2

    def returnNumber(self):
        return self.number


var = NumberHolder(7)
print(var.returnNumber())  # Prints '14'
