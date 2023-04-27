# <--DATA TYPES-->



# --> Strings

# "I'm a string" -double quotes
# 'Me too' -single quotes
# str("I'm a string") -str() constructor function

as_well = "also" # Assinging a string to a variable
print(f"I'm a string {as_well}") # Using f-string for string interpolation

# `Backticks` are not used in Python, use f-string instead

# Advanced Formatting using f-string
price_1 = 3
price_2 = 2.5

print(f"Item 1 costs ${price_1:.2f}")
# => Item 1 costs $3.00
print(f"Item 2 costs ${price_2:.2f}")
# => Item 2 costs $2.50

# You can run methods on strings because they're part of the String class in Python

type("hello")
# => <class 'str'>

"hello"
# "hello"
"hello".upper()
# "HELLO"
"HELLO".lower()
# "hello"
"hello".capitalize()
# "Hello"
"hello" + "world"
# "helloworld"
"hello" * 3
# "hellohellohello"

# Using dir() function lists all methods that can be applied to given object
dir("hello")
# => ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', etc. ]
# Methods with double underscores are magic methods that can run automatically under certain conditions



# --> NUMBERS

# Two types of numbers in Python, Integers and Floats
# Integers are whole numbers like 1, 2, 3
# Floats are decimal numbers 0.1, 12.98, 4.3333333

# You can convert some other types by using int() or float() constructor functions

int("1") # string to int
# => 1
int(1.1) # float to int
# => 1
float("1.1") # string to float
# => 1.1

# Python will convert Integers to a Float when performing math operations
4 / 3
# 1.3333333333333333
4 / 3.0
# 1.3333333333333333
float(4 / 3)
# 1.3333333333333333



# --> SEQUENCE TYPES

# Three basic sequence types are lists, tuples, ranges


# --> --> Lists

[1, 3, 400, 7] # creates a list
# => [1, 3, 400, 7]
list() # creates an empty list
# => []

# Access specific elements in a list using it's index, starting at 0
list_abc = ['a','b','c']
list_abc[0]
# => 'a'
list_abc[1]
# => 'b'
list_abc[2]
# => 'c'

# Lists are mutable and can be operated on using several functions and methods
len([1, 3, 400, 7]) # len returns the length, or number of items in a container
# 4
sorted([5, 100, 234, 7, 2]) # organizes list in ascending order
# [2, 5, 7, 100, 234]
list_123 = [1, 2, 3]
list_123.pop() # Remove and return item at index, last item default
# 3
list_123.remove(1) # removes first occurrence of value given
''' 
Since the 3 was removed in above pop() method and now /
the first occurrence of the number 1 was removed, we /
will only get back a list containing the only remaining number, 2. /
Also, triple quotes is a way of doing multiline comments
'''
print(list_123)
# [2]


# --> --> Tuples

'''
Tuples are created with open and close parentheses /
instead of square brackets. The tuple() constructor /
function can be used to cast lists and other / 
iterable data types to tuples. Tuples are immutable, meaning /
once it's been created, the tuple itself cannot change.
'''

(1, 2, 3) # creates a tuple
# => (1, 2, 3)
tuple([1, 2, 3]) # casts a list into a tuple
# => (1, 2, 3)

'''
NOTE: Parentheses can also be used for order of operations / 
and grouping statements. To let Python know that it's looking / 
at a tuple, there has to be at least one comma- even in /
tuples with only one element
'''

(1,) # creates a tuple with one element, requires at least one comma



# <--Sets and Dicts->>


# >>> Sets
'''
A set is unindexed, unordered, and unchangeable. It can be / 
initiated with curly brackets or the set() class constructor. / 
The set() class constructor takes a list or tuple as its only argument / 
(remember those brackets and parentheses!) The elements of a set are uniqueS
'''

set() # creates an empty set
# => {}
set(3, 2, 3, 'a', 'b', 'a')
# => TypeError: set expected at most 1 argument, got 6
set([3, 2, 3, 'a', 'b', 'a'])
# => {2, 3, 'a', 'b'}


# >>> Dictionaries
'''
Similar to JS objects with key value pairs. Keys must be in a string format. /
Keys can only accessed with bracket notation.
'''
{ "key1": "value1", "key2": "value2" }

my_dict = { "key1": 1, "key2": 2 }
my_dict["key2"]
# => 2

my_dict = { "key1": "value1", "key2": "value2" }
print(my_dict["key3"])
# => KeyError: 'key3'

print(my_dict.get("key3"))
# => None

'''
You can also use the built-in .get() method to retrieve the value for a key. /
This is a useful method for times when you're unsure if a key exists, as it /
returns None instead of an error if no matching key exists
'''
my_dict = { "key1": "value1", "key2": "value2" }
print(my_dict["key3"])
# => KeyError: 'key3'

print(my_dict.get("key3"))
# => None

# You can also create dictionaries using the dict() class constructor.
dict(x = 1, y = 2)
# => {'x': 1, 'y': 2}



# <--NONE-->

'''
Represents absence of a value. Unlike JavaScript, Python won't let you /
create a variable without assigning a value. You must explicitly assign /
a value of None if you want an "empty" variable.
'''
# no_value
# => NameError: name 'no_value' is not defined
no_value = None
print(no_value)
# => None

# There are only two values of the Boolean data type: True and False. 
# We can confirm this by inspecting True and False with the type() function.
type(True)
# => <class 'bool'>
type(False)
# => <class 'bool'>



# <--BOOLEANS-->

'''
Only 2 types of Booleans, 'True' and 'False'
Truthy and Falsy values exist in Python as well
'''
type(True)
# => <class 'bool'>
type(False)
# => <class 'bool'>

not True
# => False
not False
# => True
not 1
# => False
not 0
# => True
not ''
# => True
not None
# => True
not []
# => True
not ()
# => True
not {}
# => True
'''
NOTE: not is the operator that reverses the truth
value of a value, variable, or statement.! still plays a
role in Python, but it is only used in the != operator
 that asserts that two values are not equal.
'''

# make sure to keep the "everything is an object" /
# principle in mind when working in Python