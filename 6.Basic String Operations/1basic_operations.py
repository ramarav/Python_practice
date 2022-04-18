myString = "Hello World"
# length
print('Length of the string is %d' % (len(myString)))
# position
print('"o" is placed at %dth position in : %s' % (myString.index("o"), myString))
# count
print('"l" is present %d times in string : %s' % (myString.count('l'), myString))
# String slicing
print(myString[2:5])
print(myString[2:5:1])
# String reversal
print(myString[::-1])
# Sentence formatting
print(myString.lower())
print(myString.upper())
# starts with
print(myString.startswith("bcdedit"))
# Ends with
print(myString.endswith("d"))
# Splitting a string
print(myString.split())
