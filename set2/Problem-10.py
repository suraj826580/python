### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

tuple1 = (11, [22, 33], 44, 55)
# tuple1: (11, [222, 33], 44, 55) expected

for x in tuple1:
    if(type(x)==list):
        x[0]=222
    else:
        continue
print(tuple1)        
        
