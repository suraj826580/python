# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

file = open("./input.txt", "r")
content = file.read()
count = 0
for x in content:
    print(x)
    count = count+1
    
print(count)

file.close()
