"""
Start with print()\n
1. Syntax\n
2. Comment\n
3. Variables\n
4. Data Types\n
5. Scala Type\n
6. Array Type\n
7. Object Type\n
"""

class c1_syntax():
    """
    Syntax\n
    Indentation refers to the spaces at the beginning of a code line.\n
    \n
    Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.\n
    \n
    Python uses indentation to indicate a block of code.\n
    ```
    if 5 > 2:
        print("Five is greater than two!")
    ```
    Syntax Error:\n
    ```
    if 5 > 2:
    print("Five is greater than two!")
    The number of spaces is up to you as a programmer, but it has to be at least one.\n
    ```
    if 5 > 2:
      print("Five is greater than two!")
    if 5 > 2:
            print("Five is greater than two!")
    ```
    You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:\n
    ```
    if 5 > 2:
        print("Five is greater than two!")
                print("Five is greater than two!")
    ```
    """

class c2_comment():
    """
    Comment\n
    Comments can be used to explain Python code.\n
    Comments can be used to make the code more readable.\n
    Comments can be used to prevent execution when testing code.\n
    ```
    #This is a comment.
    \"\"\"
    This is a documentation comment
    \"\"\"
    print("Hello, World!") # This shit is also a comment!
    # This below line will not be executed
    # print("Ah Yeahoo!")
    ```
    """

class c3_variables():
    """
    Variables\n
    Variables are containers for storing data values.\n
    Python has no command for declaring a variable.\n
    A variable is created the moment you first assign a value to it.\n
    ```
    # Example:
    x = 5
    y = "John"
    print(x)
    print(y)
    ```
    Variables do not need to be declared with any particular type, and can even change type after they have been set.\n
    ```
    x = 4       # x is of type int
    x = "Sally" # x is now of type str
    print(x)
    ```
    If you want to specify the data type of a variable, this can be done with casting.\n
    ```
    x = str(3)    # x will be '3'
    y = int(3)    # y will be 3
    z = float(3)  # z will be 3.0
    ```
    You can get the data type of a variable with the type() function.\n
    ```
    x = 5
    y = "John"
    print(type(x))
    print(type(y))
    ```
    String variables can be declared either by using single or double quotes:\n
    ```
    x = "John"
    # is the same as
    x = 'John'
    ```
    Variable names are case-sensitive.\n
    ```
    a = 4
    A = "Sally"
    #A will not overwrite a
    print(a)
    print(A)
    ```
    Illegal variable names:\n
    ```
    2myvar = "John"
    my-var = "John"
    my var = "John"
    ```
    """

class c4_data_types():
    """
    Data Types\n
    In programming, data type is an important concept.\n
    Variables can store data of different types, and different types can do different things.\n
    Python has the following data types built-in by default, in these categories:\n
    Text Type:	```str```\n
    Numeric Types:	```int```, ```float```, ```complex```\n
    Sequence Types:	```list```, ```tuple```, ```range```\n
    Mapping Type:	```dict```\n
    Set Types:	```set```, ```frozenset```\n
    Boolean Type:	```bool```\n
    Binary Types:	```bytes```, ```bytearray```, ```memoryview```\n
    """

class c5_scala_type():
    """
    Scala Type\n
    1. Text\n
    2. Numbers:\n
        2.1. integer (int)\n
        2.2. float (float)\n
        2.3. complex (complex)\n
    """

class c6_array_type():
    """
    Array Type\n
    Right now we can use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the ```NumPy library```.\n
    An array is a special variable, which can hold more than one value at a time.\n
    If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:\n
    ```
    car1 = "Ford"
    car2 = "Volvo"
    car3 = "BMW"
    ```
    However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?\n
    The solution is an array!\n
    An array can hold many values under a single name, and you can access the values by referring to an index number.\n
    Get the value of the first array item:\n
    ```
    x = cars[0]
    ```
    Modify the value of the first array item:\n
    ```
    cars[0] = "Toyota"
    ```
    Return the number of elements in the cars array:\n
    ```
    x = len(cars)
    ```
    Print each item in the cars array:\n
    ```
    for x in cars:
        print(x)
    ```
    Add one more element to the cars array:\n
    ```
    cars.append("Honda")
    ```
    Delete the second element of the cars array:\n
    ```
    cars.pop(1)
    ```
    """


