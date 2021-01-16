"""
```
mytuple = ("apple", "banana", "cherry")
```
Tuple\n
Tuples are used to store multiple items in a single variable.\n
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.\n

A tuple is a collection which is ordered and unchangeable.\n
"""

def m0_tuples_properties():
    """
    Tuple Items\n
    Tuple items are ordered, unchangeable, and allow duplicate values.\n

    Tuple items are indexed, the first item has index [0], the second item has index [1] etc.\n

    Ordered\n
    When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.\n

    Unchangeable\n
    Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.\n

    Allow Duplicates\n
    Since tuple are indexed, tuples can have items with the same value:\n
    ```
    # Tuples allow duplicate values:
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)
    ```
    Tuple Length\n
    To determine how many items a tuple has, use the len() function:\n
    ```
    # Print the number of items in the tuple:
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))
    ```
    Create Tuple With One Item\n
    To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.\n
    ```
    # One item tuple, remember the commma:
    thistuple = ("apple",)
    print(type(thistuple))

    #NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))
    ```
    Tuple Items - Data Types\n
    Tuple items can be of any data type:\n
    ```
    # String, int and boolean data types:
    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = (True, False, False)
    ```
    A tuple can contain different data types:\n
    ```
    # A tuple with strings, integers and boolean values:
    tuple1 = ("abc", 34, True, 40, "male")
    ```
    ```type()```
    From Python's perspective, tuples are defined as objects with the data type 'tuple':\n
    ```
    <class 'tuple'>
    ```
    ```
    # What is the data type of a tuple?
    mytuple = ("apple", "banana", "cherry")
    print(type(mytuple))
    ```
    The tuple() Constructor\n
    It is also possible to use the tuple() constructor to make a tuple.\n
    ```
    # Using the tuple() method to make a tuple:
    thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
    print(thistuple)
    ```
    """

def m1_access_tuple_items():
    """
    Access Tuple Items\n
    You can access tuple items by referring to the index number, inside square brackets:\n
    ```
    # Print the second item in the tuple:
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])
    ```
    Note: The first item has index ```0```.\n

    Negative Indexing\n
    Negative indexing means start from the end.\n

    -1 refers to the last item, -2 refers to the second last item etc.\n
    ```
    # Print the last item of the tuple:
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[-1])
    ```
    Range of Indexes\n
    You can specify a range of indexes by specifying where to start and where to end the range.\n

    When specifying a range, the return value will be a new tuple with the specified items.\n
    ```
    # Return the third, fourth, and fifth item:
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[2:5])
    ```
    Note: The search will start at index 2 (included) and end at index 5 (not included).\n
    Remember that the first item has index 0.\n
    By leaving out the start value, the range will start at the first item:\n
    ```
    # This example returns the items from the beginning to, but NOT included, "kiwi":
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[:4])
    ```
    By leaving out the end value, the range will go on to the end of the list:\n
    ```
    # This example returns the items from "cherry" and to the end:
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[2:])
    ```
    Range of Negative Indexes\n
    Specify negative indexes if you want to start the search from the end of the tuple:\n
    ```
    # This example returns the items from index -4 (included) to index -1 (excluded)
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[-4:-1])
    ```
    Check if Item Exists\n
    To determine if a specified item is present in a tuple use the in keyword:\n
    ```
    # Check if "apple" is present in the tuple:
    thistuple = ("apple", "banana", "cherry")
    if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
    ```
    """

def m2_update_tuples():
    """
    Tuples are unchangeable, meaing that you cannot change, add, or remove items once the tuple is created.\n
    But there are some workarounds.\n
    Change Tuple Values\n
    Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.\n
    But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.\n
    ```
    # Convert the tuple into a list to be able to change it:
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    print(x)
    ```
    Add Items\n
    Once a tuple is created, you cannot add items to it.\n
    ```
    # You cannot add items to a tuple:
    thistuple = ("apple", "banana", "cherry")
    thistuple.append("orange") # This will raise an error
    print(thistuple)
    ```
    Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.\n
    ```
    # Convert the tuple into a list, add "orange", and convert it back into a tuple:
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.append("orange")
    thistuple = tuple(y)
    ```
    Remove Items\n
    Note: You cannot remove items in a tuple.\n

    Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:\n
    ```
    # Convert the tuple into a list, remove "apple", and convert it back into a tuple:
    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.remove("apple")
    thistuple = tuple(y)
    ```
    Or you can delete the tuple completely:\n
    ```
    # The del keyword can delete the tuple completely:
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple) #this will raise an error because the tuple no longer exists
    ```
    """

def m4_unpack_tuples():
    """
    Unpacking a Tuple\n
    When we create a tuple, we normally assign values to it. This is called "packing" a tuple:\n
    ```
    # Packing a tuple:
    fruits = ("apple", "banana", "cherry")
    ```
    But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":\n
    ```
    # Unpacking a tuple:
    fruits = ("apple", "banana", "cherry")
    (green, yellow, red) = fruits
    print(green)
    print(yellow)
    print(red)
    ```
    Note: The number of variables must match the number of values in the tuple, if not, you must use an asterix to collect the remaining values as a list.\n

    Using Asterix*\n
    If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:\n
    ```
    # Assign the rest of the values as a list called "red":

    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

    (green, yellow, *red) = fruits

    print(green)
    print(yellow)
    print(red)
    ```
    If the asterix is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.\n
    ```
    # Add a list of values the "tropic" variable:

    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

    (green, *tropic, red) = fruits

    print(green)
    print(tropic)
    print(red)
    ```
    """

def m5_loop_through_tuple_items():
    """
    Loop Through a Tuple\n
    You can loop through the tuple items by using a for loop.\n
    ```
    # Iterate through the items and print the values:
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
    print(x)
    ```
    Learn more about for loops in our Python For Loops Chapter.\n
    Loop Through the Index Numbers\n
    You can also loop through the tuple items by referring to their index number.\n
    Use the ```range()``` and ```len()``` functions to create a suitable iterable.\n
    ```
    # Print all items by referring to their index number:
    thistuple = ("apple", "banana", "cherry")
    for i in range(len(thistuple)):
    print(thistuple[i])
    ```
    Using a ```While``` Loop\n
    You can loop through the list items by using a ```while``` loop.\n

    Use the ```len()``` function to determine the length of the tuple, then start at ```0``` and loop your way through the tuple items by refering to their indexes.\n

    Remember to increase the index by 1 after each iteration.\n
    ```
    # Print all items, using a while loop to go through all the index numbers:
    thistuple = ("apple", "banana", "cherry")
    i = 0
    while i < len(thistuple):
        print(thistuple[i])
        i = i + 1
    ```
    """

def m6_join_tuples():
    """
    Join Two Tuples\n
    To join two or more tuples you can use the ```+``` operator:\n
    ```
    # Join two tuples:
    tuple1 = ("a", "b" , "c")
    tuple2 = (1, 2, 3)

    tuple3 = tuple1 + tuple2
    print(tuple3)
    ```
    Multiply Tuples\n
    If you want to multiply the content of a tuple a given number of times, you can use the ```*``` operator:\n
    ```
    # Multiply the fruits tuple by 2:
    fruits = ("apple", "banana", "cherry")
    mytuple = fruits * 2

    print(mytuple)
    ```
    """

def m7_tuple_methods():
    """
    Tuple Methods\n
    Python has two built-in methods that you can use on tuples.\n

    ```
    # Method	Description
    count()	Returns the number of times a specified value occurs in a tuple
    index()	Searches the tuple for a specified value and returns the position of where it was found
    ```
    """