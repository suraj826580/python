# ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
def Fun(numbers):
    for x in numbers:
        if(x>500):
            break
        elif (x%5==0 and x<=150):
            print(x)
        
Fun(numbers)
