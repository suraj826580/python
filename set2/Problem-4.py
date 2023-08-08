### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

str = "PyNaTive"
def print_Smaller_Char_First(str):
    lowerStr=''
    upperStr=''
    for x in str:
        if (x.islower()):
            lowerStr+=x
        else:
            upperStr=upperStr+x
    return lowerStr + upperStr
result=print_Smaller_Char_First(str)
print(result)
