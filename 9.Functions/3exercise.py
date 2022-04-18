def animals_list():
    mylist = ['dog', 'cat', 'tiger', 'deer', 'lion', 'elephant']
    return mylist


def category_list(info):
    return "%s is an animal" % info


def animal_category():
    list_animal = animals_list()
    for i in list_animal:
        print(category_list(i))


animal_category()
