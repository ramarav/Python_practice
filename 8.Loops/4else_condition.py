"""
Unlike languages like C,CPP.. we can use else for loops. 
When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
If a break statement is executed inside the for loop then the "else" part is skipped. 
Note that the "else" part is executed even if there is a continue statement.
"""
count=0
while count<5:
    print(count)
    count+=1
else:
    print('End of code')
for x in range(10):
    print(x)
    if x==9:
        break
    else:
        print('It will be printed')
else:
        print('It wont be printed')