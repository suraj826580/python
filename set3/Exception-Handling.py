# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def numberDiv(num1, num2):
    try:
        result = num1/num2
        return result
    except:
        print("Cannot divide by zero.")


ans = numberDiv(5, 0)
print(ans)
