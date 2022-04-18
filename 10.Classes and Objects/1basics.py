# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.
class MyClass:
    MyVar = 12

    def MyFunc(self):
        return 'This is cool'


MyObject = MyClass()
print(MyObject.MyVar)
print(MyObject.MyFunc())
