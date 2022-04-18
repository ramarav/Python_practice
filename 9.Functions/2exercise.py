"""
In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", 
"Allowing programmers to share and connect code together"
Add a function named build_sentence(info) which receives a single argument containing a string 
and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
Run and see all the functions work together!
"""
def list_benefits():
    myList = ["More organized code", "More readable code", "Easier code reuse","Allowing programmers to share and connect code together"]
    return myList
def build_sentence(info):
    print('%s  is a benefit of functions!'%info)
def benefits_of_functions():
    list_of_benefits = list_benefits()
    for x in list_of_benefits:
        print(build_sentence(x))

benefits_of_functions()

def animals_list():
    myList=['dog','cat','tiger','deer','lion','elephant']
    return myList

def catogory_list(info):
    return "%s is an animal"%info
def animal_category():
    list_animal = animals_list()
    for i in list_animal:
        return catogory_list(i)
animal_category()