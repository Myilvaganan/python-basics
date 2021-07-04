print(2*5)

""" Simple Data Types """
# String
string = 'myil'

# Number
num = 4

# Float
floatNum = 4.4

""" Compound Data Types """
# Lists

lists = [4, 5, 'myil', 6.7, [1, 2, 4, 'myil']]

""" find length and sum the list """
# Know the default methods using dir(str) or dir(int) or dir(list)

student_grades = [3.5, 6.7, 89.7]

mySum = sum(student_grades)
length = len(student_grades)

mean = mySum / length

print(mean)

# Dictionary Data Type

dic_data = {"myil": 80, "ram": 96.52, "krish": 89.63}

print(sum(dic_data.values()))
print(dic_data.keys())


# tupels
# like array which is immutable

tuple_data = (1, 4, 5)


""" Functions  (use def keyword at the begining) """


def foo(n):
    return n*n


print(foo(5))


""" conditional """

# If else statement
if 4 == 4:
    print(True)
else:
    print(False)

# and operator

if 4 == 4 and 5 == 6:
    print("Printed")
else:
    print("Failed")

# or operator

if 4 == 9 or 5 == 5:
    print("Printed")
else:
    print("Failed")


""" Example Condition with function """


def mean(value):
    if isinstance(value, dict):
        print('It is dict')
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean


mon = [8.5, 6.5, 4.4, 2.2, 36.2]

student_grades = {"Myil": 89.5, "Ram": 99.6, "Krishna": 100.00}

print(mean(student_grades))
print(mean(mon))


# Elif statement

def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"


# To know the input types

"""  
isinstance("abc", str) !check with string
isinstance([1, 2, 3], list) !check with list

type("abc") == str  !check with string
type([1, 2, 3]) == lst  !check with list
"""


# User Input using 'input' keyword

def temp(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'


""" userInput = input('Enter Temperature: ')
temp(userInput) """

""" The above function shows error because user input is always string, should change it type while working with int or change the type of user input itself """


def temp1(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'


# userInput1 = float(input('Enter Temperature: '))
# print(temp1(userInput1))


""" String Formatting """

# stringStr = input('Enter your name: ')
""" Method - 1 - older version 3.3, 2.2, 1 """
# message = "Hello %s" % stringStr
""" Method - 2 - Modern version 3.9 """
# message1 = f"Hello {stringStr}"

# print(message1)

# multiple inputs


# name = input('Enter your name: ')
# lname = input('Enter your lanme: ')
""" Method - 1 - older version 3.3, 2.2, 1 """
# message = "Hello %s %s" % (name, lname)
""" Method - 2 - Modern version 3.9 """
# message1 = f"Hello {name,lname}"

""" Another Method """
name = "Sim"
experience_years = 1.5
# print("Hi {}, you have {} years of experience".format(name, experience_years))

""" For Loop """

# looping through list
monday_temp = [5.2, 9.8, 3.4, 6.7]
for temp in monday_temp:
    print(round(temp))


# looping through string
string_loop = "myilvaganan"
for letter in string_loop:
    print(letter.title())

# looping through dictionary

marks = {"Myil": 89.5, "Ram": 99.6, "Krishna": 100.00}


for grades in marks.items():
    print(grades)  # return tupels

for grades in marks.keys():
    print(grades)  # return tupels

for grades in marks.values():
    print(grades)  # return tupels

"""  ---------output----------
('Myil', 89.5)
('Ram', 99.6)
('Krishna', 100.0) 
Myil
Ram
Krishna
89.5
99.6
100.0
"""
phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))


phone_numbers = {"John Smith": "+37682929928",
                 "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))

""" While Loop """

username = ''

while username != 'mymy':
    username = input("Enter Username: ")


while True:
    username = input("Enter Username: ")
    if username == 'py':
        break
    else:
        continue

""" Uncomment import datetime for execution """

#import datetime

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")


# multiple arguments in functions

def area(a, b):
    return a + b


#keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=3, b=5, c=1))

#non-keyword arguments


def find_sum(*args):
    return sum(args)


print(find_sum(1,4,6))


""" Changing input to uppercase and  sorted"""

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)

""" Return the average of multiple args avr(2,3,5,9,7) """

def avr(*args):
    return sum(args) / len(args)


""" Functions can have default parameters(e.g. coefficient): """


def converter(feet, coefficient=3.2808):
    meters = feet / coefficient
    return meters


print(converter(10))


""" Arguments can be passed as non-keyword(positional) arguments(e.g. a) or keyword arguments(e.g. b=2 and c=10): """


def volume(a, b, c):
    return a * b * c


print(volume(1, b=2, c=10))


""" An * args parameter allows the  function to be called with an arbitrary number of non-keyword arguments: """


def find_max(*args):
    return max(args)


print(find_max(3, 99, 1001, 2, 8))

""" An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
 """
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

""" Output: Sim """
