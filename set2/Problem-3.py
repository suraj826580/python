import math
### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.


def Concat(str1,str2):
    str3=''
    halfLength=int(len(str1)/2)
    for x,y in enumerate(str1):
        if(x==2):
            str3=str3+str2+y
        else:
            str3+=y    
    print(str3)
Concat("AuLt","Kelly")
