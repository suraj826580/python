def strReverseFun1(input):
    """Reverses the string in-place."""
    return input[::-1]
result=strReverseFun1("Python")
print(result)



def strReverseFun2(input):
    """Reverses the string in-place."""
    reversedStr=''
    for x in input:
        reversedStr= x+reversedStr
    return reversedStr
Secondresult=strReverseFun2("Masai School")
print(Secondresult)