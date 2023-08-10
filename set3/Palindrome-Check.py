# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def checkPallindrom(input):
    reverseInput = input[::-1]
    if(input==reverseInput):
        return f"The word {input} is a palindrome."
    else:
        return f"The word {input} is not a palindrome."

        

result=checkPallindrom("madam")  
print(result)