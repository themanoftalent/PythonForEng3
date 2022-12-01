Author : Mehmet Akif CIFCI
Here we will cover up some Python basics and some useful libraries for data science.
we will focus on Python 3.11.0
# Python Basics
## Variables
Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
## Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
## Getting the Data Type
You can get the data type of any object by using the type() function:
## Setting the Data Type
In Python, the data type is set when you assign a value to a variable:
## Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
## Numbers
Python supports two types of numbers - integers and floating point numbers.
(Integers are positive or negative whole numbers with no decimal point. Floats are positive or negative numbers containing one or more decimals.)
## Integers
Integers are whole numbers, positive or negative, without decimals, of unlimited length.
## Floats
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
## Casting
If you want to specify a type on to a variable this can be done with casting.
## Strings
Strings in Python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
Strings can be output to screen using the print function. For example: print("Hello")
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
## Booleans
Booleans represent one of two values: True or False.
## Lists
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
## Access Items
You access the list items by referring to the index number:
## Negative Indexing
    
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
## Range of Indexes
    
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.
## Change Item Value

To change the value of a specific item, refer to the index number:
## Loop Through a List
You can loop through the list items by using a for loop:
## Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
## List Length
To determine how many items a list has, use the len() method:
## Add Items
To add an item to the end of the list, use the append() method:
## Remove Item
There are several methods to remove items from a list:
The del keyword removes the specified index:
The pop() method removes the specified index, (or the last item if index is not specified):
The remove() method removes the specified item:
he clear() method empties the list:
## The list() Constructor
It is also possible to use the list() constructor when creating a new list.
## Tuples
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
## Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:
## Negative Indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
## Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
## Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
## Loop Through a Tuple
You can loop through the tuple items by using a for loop.
## Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:
## Tuple Length
To determine how many items a tuple has, use the len() method:
## Add Items
Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
## Remove Items
Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
## The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
## Sets
A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.
## Access Items
You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
## Change Items
Once a set is created, you cannot change its items, but you can add new items.
## Add Items
To add one item to a set use the add() method.
To add more than one item to a set use the update() method.
## Get the Length of a Set
To determine how many items a set has, use the len() method.
## Remove Item
To remove an item in a set, use the remove(), or the discard() method.
## The set() Constructor
It is also possible to use the set() constructor to make a set.
## Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is unordered, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:
## Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:
There is also a method called get() that will give you the same result:
## Change Values
You can change the value of a specific item by referring to its key name:
## Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
## Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:
## Dictionary Length
To determine how many items (key-value pairs) a dictionary has, use the len() method.
## Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
## Removing Items
There are several methods to remove items from a dictionary:
The pop() method removes the item with the specified key name:
The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
The del keyword removes the item with the specified key name:
The del keyword can also delete the dictionary completely:
The clear() keyword empties the dictionary:
## The dict() Constructor
It is also possible to use the dict() constructor to make a new dictionary:
## If ... Else
If you want to execute a block of code if a certain condition is true, use the if statement:

