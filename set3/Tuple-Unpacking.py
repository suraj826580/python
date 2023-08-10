# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."
x = [("John", 25), ("Jane", 30)]

for y in x :
    print(f"{y[0]} is {y[1]} years old")
