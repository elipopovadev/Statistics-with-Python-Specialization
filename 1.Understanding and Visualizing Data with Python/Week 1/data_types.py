import math

'''
Data Types in Python

The following data types can be used in base python:

    boolean
    integer
    float
    string
    list
    None
    complex
    object
    set
    dictionary

Numerical or Quantitative (taking the mean makes sense)

    Discrete
        Integer (int) #Stored exactly
    Continuous
        Float (float) #Stored similarly to scientific notation. Allows for decimal places but loses precision.
'''

print(type(4))  # <class 'int'>
print(type(0))  # <class 'int'>
print(type(-3))  # <class 'int'>

print(3/5)  # 0.6
print(type(3/5))  # <class 'float'>
print(type(math.pi))  # <class 'float'>
print(type(4.0))  # <class 'float'>

# Try taking the mean
numbers = [math.pi, 3/5, 4.1]
print(numbers)  # [3.141592653589793, 0.6, 4.1]
type(sum(numbers)/len(numbers))  # float

'''
Categorical or Qualitative

    Nominal
        Boolean (bool)
        String (str)
        None (NoneType)
    Ordinal
        Only defined by how you use the data
        Often important when creating visuals
        Lists can hold ordinal information because they have indices
'''

# Boolean
print(type(True))  # <class 'bool'>

if 6 > 5:
    print("Yes!")

myList = [True, 6 < 5, 1 == 3, None is None]
for element in myList:
    print(type(element))  # <class 'bool'>

print(sum(myList)/len(myList))  # 0.5
print(type(sum(myList)/len(myList)))  # <class 'float'>

# String
print(type("This sentence makes sense"))  # <class 'str'>
print(type("Makes sentense this sense"))  # <class 'str'>
print(type("math.pi"))  # <class 'str'>

strList = ['dog', 'koala', 'goose']
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(sum(strList)/len(strList))

# Nonetype
print(type(None))  # <class 'NoneType'>
x = None
print(type(x))  # <class 'NoneType'>

noneList = [None]*5
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
sum(noneList)/len(noneList)

'''
Lists

A list can hold many types and can also be used to store ordinal information.
'''
myList = [1, 1.1, "This is a sentence", None]
for element in myList:
    print(type(element))
# TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(sum(myList)/len(myList))

# List
myList = [1, 2, 3]
for element in myList:
    print(type(element))
print(sum(myList)/len(myList))  # note that this outputs a float

myList = ['third', 'first', 'medium', 'small', 'large']
print(myList[0])  # 'third'

myList.sort()
print(myList)  # ['first', 'large', 'medium', 'small', 'third']
