"""
Dictionaries can be iterated over, just like a list.
However, a dictionary, unlike a list, does not keep the order of the values stored in it.
"""
phonebook = {"Rama": 9848, "Rao": 9948, "Mekala": 9949}
for item, value in phonebook.items():
    print('%d is the contact number of %s' % (value, item))
