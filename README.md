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
## Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
## Else
The else keyword catches anything which isn't caught by the preceding conditions.
## Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.
## Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
## And
The and keyword is a logical operator, and is used to combine conditional statements:
## Or
The or keyword is a logical operator, and is used to combine conditional statements:
## Nested If
You can have if statements inside if statements, this is called nested if statements.
## While Loops
With the while loop we can execute a set of statements as long as a condition is true.
## Break Statement
With the break statement we can stop the loop even if the while condition is true:
## Continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
## Else
With the else statement we can run a block of code once when the condition no longer is true:
## For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
## Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:
## The break Statement
With the break statement we can stop the loop before it has looped through all the items:
## The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:
## The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
## Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
## Nested Loops
A nested loop is a loop inside a loop.
The "inner loop" will be executed one time for each iteration of the "outer loop":
## The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
## Functions
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
## Creating a Function
In Python a function is defined using the def keyword:
## Calling a Function
To call a function, use the function name followed by parenthesis:
## Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
## Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
## Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
## Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:
## Keyword Arguments
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
## Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
## Default Parameter Value
The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:
## Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:
## Return Values
To let a function return a value, use the return statement:
## The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
## Recursion
Python also accepts function recursion, which means a defined function can call itself.
## Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
## The yield Statement
The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
## Scope
Scope determines the visibility of variables. Variables that are created inside a function belongs to the local scope of that function, and can only be used inside that function.
## Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
## Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
## Naming Variables
Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
Variable names cannot start with a number.
Variable names are case-sensitive (age, Age and AGE are three different variables).
## Camel Case
Each word, except the first, starts with a capital letter:
## Pascal Case
Each word starts with a capital letter:
## Snake Case
Each word is separated by an underscore character:
## List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
## Set Comprehension
Set comprehension offers a shorter syntax when you want to create a new set based on the values of an existing set.
## Dictionary Comprehension
Dictionary comprehension offers a shorter syntax when you want to create a new dictionary based on the values of an existing dictionary.
## Modules
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
## Create a Module
To create a module just save the code you want in a file with the file extension .py
## Import a Module
Now we can use the module we just created, by using the import statement:
## Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
## Naming a Module
You can name the module file whatever you like, but it must have the file extension .py
## Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
## Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
## Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
## Import From Module
You can choose to import only parts from a module, by using the from keyword.
## Random Module
The random module can be used to generate random numbers:
## Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
## Get Current Date
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
## The strftime() Method
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
## The strptime() Method
The datetime object has a method for parsing dates from strings into date objects.
The method is called strptime(), and takes two parameters, date_string, and format, to specify the format of the date string:
## The timedelta() Object
The timedelta object represents a duration, the difference between two dates or times.
## Python JSON
JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
## Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.
The result will be a Python dictionary.
## Convert from Python to JSON
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
## Format the Result
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() method has parameters to make it easier to read the result:
## Order the Result
The json.dumps() method has parameters to order the keys in the result:
## Convert Python Objects into JSON strings
Python has built-in data types for dictionaries, lists, tuples, strings, integers, and floats.
## Convert a Python Object containing all the legal data types
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

## Python PIP
PIP is a package manager for Python packages, or modules if you like.
## What is a Package?
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.
## Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:
## Download a Package
Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
## Find Packages
PIP has a command to list all packages currently installed on your system:
## Remove a Package
Use the uninstall command to remove a package:
## Python Try Except
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
## Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
## The AssertionError Exception
The AssertionError exception is raised when an assert statement fails.
## The AttributeError Exception
The AttributeError exception is raised when attribute assignment or reference fails.
## The EOFError Exception
The EOFError exception is raised when the input() function hits an end-of-file condition (EOF) without reading any data.
## The FloatingPointError Exception
The FloatingPointError exception is raised when a floating point operation fails.
## The GeneratorExit Exception
The GeneratorExit exception is raised when a generator's close() method is called.
## The ImportError Exception
