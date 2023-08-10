# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

class Manager:
    def __init__(self):
        self.dic = {}

    def add_name_age(self, name, age):
        self.dic[name] = age

    def add_age(self, name, age):
        if name in self.dic:
            self.dic[name] = age

    def delete_name(self, name):
        if name in self.dic:
            del self.dic[name]

    def __str__(self):
        return str(self.dic)


res1 = Manager()
print(res1)
res1.add_name_age("John", 25)
res1.add_age("John", 26)
print(res1)
res1.delete_name("John")
print(res1)
