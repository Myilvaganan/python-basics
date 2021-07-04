# Lists - More on  Learning

# List Methods

""" ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] """


my_random_data = [1, 4, 6, 56, 85, 42, 23,
                  35, 26, 6, 6, 6, 6, 6, 31, 12, 45, 68, 95]

""" pop() =>  Removes and Returns the last element of the list"""
my_random_data.pop()  # 95
print(my_random_data)  # [1, 4, 6, 56, 85, 42, 23, 35, 26, 31, 12, 45, 68]

""" reverse() => Reverse the list """
my_random_data.reverse()
print(my_random_data)  # [68, 45, 12, 31, 26, 35, 23, 42, 85, 56, 6, 4, 1]

"""  sort() => sort the list in ascending order by default"""
my_random_data.sort()
print(my_random_data)  # [1, 4, 6, 12, 23, 26, 31, 35, 42, 45, 56, 68, 85]

""" count(ele) => counts the number of  element's occurrence in the list as a single number """
print(my_random_data.count(6))  # 6 (number of times appeared in the list)

""" append(ele) => append a new element in the list (in the last position"""
my_random_data.append(1000)
# [1, 4, 6, 6, 6, 6, 6, 6, 12, 23, 26, 31, 35, 42, 45, 56, 68, 85, 1000]
print(my_random_data)


""" index(ele) => Return the first index number of the given element in the list , starts from 0 """
""" index(self, value, start=0, stop=92233720....) """
print(my_random_data.index(1000))  # 18


""" len(input) => return the length of the list , starts from 1  """
print(len(my_random_data))  # 19

""" clear() => delete all the elements in the list, and size will become undefined """
# my_random_data.clear()
print(my_random_data)  # []


""" Access List elements """

# In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]  # Output: ['Tue', 'Wed', 'Thu']


# First three items of a list:

days[:3]  # Output: ['Mon', 'Tue', 'Wed']

# Last three items of a list:

days[-3:]  # Output: ['Fri', 'Sat', 'Sun']

# Everything but the last:

days[:-1]  # Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


# Everything but the last two:
days[:-2]  # Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


# A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpsons": "+423998200919"}
phone_numbers["Marry Simpsons"]  # Output: '+423998200919'


# List comprehension

temps = [145, 25, 584, -999]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)

""" Instead of writing above, we can create the list on the fly """

new_temps = [temp/10 for temp in temps]


new_temps = [temp / 10 for temp in temps if temp != -999]

""" for if else, we have to write for loop at last """

new_temps = [temp / 10 if temp != -999 else 0 for temp in temps]
print(f"{new_temps} line no: 91")

""" returns only int type """


def foo(list):
    new_list = [i for i in list if isinstance(i, int)]
    return new_list


""" return only numbers greater than 0 """


def foo(list):
    return [i for i in list if i > 0]


""" returns int and zero (instead of string) """


def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]


def foo(list):
    return [i if isinstance(i, int) else 0 for i in list]


""" sum of lists by type conversion """


def foo(list):
    return sum([float(i) for i in list])
