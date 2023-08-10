# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     # - *Output*: "[0, 1]"


list = [2, 7, 11, 15]
target = 9
index = []
for x, y in enumerate(list):
    for j in list:
        if (y+j == target):
            index.append(x)
            break
print(index)