"""
break is used to exit a for loop or a while loop, 
whereas continue is used to skip the current block, 
and return to the "for" or "while" statement.
"""

count =0
while count<5:
    print(count)
    count+=1
    if count==5:
        break


for x in range(20):
    if x%2 ==0:
        continue
    print(x)
