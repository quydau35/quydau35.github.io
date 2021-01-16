"""
Lists are used to store multiple items in a single variable.\n
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.\n
There are four collection data types in the Python programming language:\n

List is a collection which is ordered and changeable. Allows duplicate members.\n
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.\n
Set is a collection which is unordered and unindexed. No duplicate members.\n
Dictionary is a collection which is unordered and changeable. No duplicate members.\n
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.\n
"""

def m1_list_initiation():
    """
    Create a List:\n
    ```
    thislist = ["apple", "banana", "cherry"]
    print(thislist)
    ```

    List items are ordered, changeable, and allow duplicate values.\n
    List items are indexed, the first item has index ```[0]```, the second item has index ``[1]`` etc \n

    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.\n
    If you add new items to a list, the new items will be placed at the end of the list.\n

    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.\n

    Since lists are indexed, lists can have items with the same value:\n
    ```
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)
    ```

    To determine how many items a list has, use the ```len()``` function:\n
    ```
    # Print the number of items in the list:
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))
    ```

    List items can be of any data type:\n
    ```
    String, int and boolean data types:
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]
    ```
    A list can contain different data types:\n
    ```
    # A list with strings, integers and boolean values:
    list1 = ["abc", 34, True, 40, "male"]
    ```

    From Python's perspective, lists are defined as objects with the data type 'list':\n
    ```
    <class 'list'>
    ```

    The ```list()``` Constructor
    ```
    # Using the list() constructor to make a List:
    thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
    print(thislist)
    ```
    """

def m2_access_list_items():
    """
    Print the second item of the list:\n
    ```
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])
    ```
    Negative indexing means start from the end ```-1``` refers to the last item, ```-2``` refers to the second last item etc.\n

    You can specify a range of indexes by specifying where to start and where to end the range.\n
    When specifying a range, the return value will be a new list with the specified items.\n
    ```
    # Return the third, fourth, and fifth item:
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])
    ```
    Note: The search will start at index 2 (included) and end at index 5 (not included).\n
    Remember that the first item has index 0.\n
    By leaving out the start value, the range will start at the first item:\n
    ```
    # This example returns the items from the beginning to, but NOT including, "kiwi":
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])
    ```
    By leaving out the end value, the range will go on to the end of the list:\n
    ```
    # This example returns the items from "cherry" to the end:
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])
    ```
    Range of Negative Indexes:\n
    ```
    # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])
    ```
    To determine if a specified item is present in a list use the ```in``` keyword:\n
    ```
    # Check if "apple" is present in the list:
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")
    ```
    """

def m3_change_list_item():
    """
    To change the value of a specific item, refer to the index number:\n
    ```
    # Change the second item:
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)
    ```
    To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:\n
    ```
    # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    thislist[1:3] = ["blackcurrant", "watermelon"]
    print(thislist)
    ```
    If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:\n
    ```
    # Change the second value by replacing it with two new values:
    thislist = ["apple", "banana", "cherry"]
    thislist[1:2] = ["blackcurrant", "watermelon"]
    print(thislist)
    ```
    Note: The length of the list will change when the number of items inserted does not match the number of items replaced.\n
    If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:\n
    ```
    # Change the second and third value by replacing it with one value:
    thislist = ["apple", "banana", "cherry"]
    thislist[1:3] = ["watermelon"]
    print(thislist)
    ```

    To insert a new list item, without replacing any of the existing values, we can use the ```insert()``` method.\n
    The ```insert()``` method inserts an item at the specified index:\n
    ```
    Insert "watermelon" as the third item:
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(2, "watermelon")
    print(thislist)
    ```
    Note: As a result of the example above, the list will now contain 4 items.\n
    """

def m4_add_list_items():
    """
    Append Items\n
    To add an item to the end of the list, use the ```append()``` method:\n
    ```
    # Using the append() method to append an item:
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)
    ```
    Insert Items\n
    To insert a list item at a specified index, use the ```insert()``` method.\n
    The ```insert()``` method inserts an item at the specified index:\n
    ```
    # Insert an item as the second position:
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)
    ```
    Note: As a result of the examples above, the lists will now contain 4 items.\n
    Extend List\n
    To append elements from another list to the current list, use the ```extend()``` method.\n
    ```
    # Add the elements of tropical to thislist:
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)
    ```
    The elements will be added to the end of the list.\n
    Add Any Iterable\n
    The ```extend()``` method does not have to append lists, you can add any iterable object (```tuples```, ```sets```, ```dictionaries``` etc.).\n
    ```
    # Add elements of a tuple to a list:
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)
    ```
    """

def m5_remove_list_items():
    """
    Remove Specified Item
    The ```remove()``` method removes the specified item.\n
    ```
    # Remove "banana":
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)
    ```
    Remove Specified Index\n
    The ```pop()``` method removes the specified index.\n
    ```
    # Remove the second item:
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)
    ```
    If you do not specify the index, the ```pop()``` method removes the last item.\n
    ```
    # Remove the last item:
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)
    ```
    The ```del``` keyword also removes the specified index:\n
    ```
    # Remove the first item:
    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)
    ```
    The ```del``` keyword can also delete the list completely.\n
    ```
    # Delete the entire list:
    thislist = ["apple", "banana", "cherry"]
    del thislist
    ```
    Clear the List\n
    The ```clear()``` method empties the list.\n
    The list still remains, but it has no content.\n
    ```
    # Clear the list content:
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)
    ```
    """

def m6_loop_lists():
    """
    Loop Through a List\n
    You can loop through the list items by using a ```for``` loop:\n
    ```
    # Print all items in the list, one by one:
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
    print(x)
    ```
    Learn more about ```for``` loops in Python ```For``` Loops Chapter.\n
    Loop Through the Index Numbers\n
    You can also loop through the list items by referring to their index number.\n
    Use the ```range()``` and ```len()``` functions to create a suitable iterable.\n
    ```
    # Print all items by referring to their index number:
    thislist = ["apple", "banana", "cherry"]
    for i in range(len(thislist)):
    print(thislist[i])
    ```
    The iterable created in the example above is ```[0, 1, 2]```.\n

    Using a While Loop\n
    You can loop through the list items by using a ```while``` loop.\n

    Use the ```len()``` function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.\n

    Remember to increase the index by 1 after each iteration.\n
    ```
    # Print all items, using a while loop to go through all the index numbers
    thislist = ["apple", "banana", "cherry"]
    i = 0
    while i < len(thislist):
        print(thislist[i])
        i = i + 1
    ```
    Learn more about ```while``` loops in Python ```While``` Loops Chapter.\n

    Looping Using List Comprehension\n
    List Comprehension offers the shortest syntax for looping through lists:\n
    ```
    # A short hand for loop that will print all items in a list:
    thislist = ["apple", "banana", "cherry"]
    [print(x) for x in thislist]
    ```
    """

def m7_list_comprehension():
    """
    List Comprehension\n
    List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.\n
    Example:\n
    Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.\n
    Without list comprehension you will have to write a for statement with a conditional test inside:\n
    ```
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
    if "a" in x:
        newlist.append(x)

    print(newlist)
    ```
    With list comprehension you can do all that with only one line of code:\n
    ```
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)
    ```
    The Syntax\n
    ```
    newlist = [expression for item in iterable if condition == True]
    ```
    The return value is a new list, leaving the old list unchanged.\n

    Condition\n
    The condition is like a filter that only accepts the items that valuate to ```True```.\n
    ```
    # Only accept items that are not "apple":
    newlist = [x for x in fruits if x != "apple"]
    ```
    The condition ```if x != "apple"``` will return ```True``` for all elements other than "apple", making the new list contain all fruits except "apple".\n

    The condition is optional and can be omitted:\n
    ```
    # With no if statement:
    newlist = [x for x in fruits]
    ```
    Iterable\n
    The iterable can be any iterable object, like a list, tuple, set etc.\n
    ```
    # You can use the range() function to create an iterable:
    newlist = [x for x in range(10)]
    ```
    Same example, but with a condition:\n
    ```
    # Accept only numbers lower than 5:
    newlist = [x for x in range(10) if x < 5]
    ```
    Expression\n
    The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:\n
    ```
    # Set the values in the new list to upper case:
    newlist = [x.upper() for x in fruits]
    ```
    You can set the outcome to whatever you like:\n
    ```
    # Set all values in the new list to 'hello':
    newlist = ['hello' for x in fruits]
    ```
    The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:\n
    ```
    # Return "orange" instead of "banana":
    newlist = [x if x != "banana" else "orange" for x in fruits]
    ```
    The expression in the example above says:\n

    "Return the item if is not banana, if it is banana return orange".\n
    """

def m8_sort_list():
    """
    Sort List Alphanumerically
    List objects have a ```sort()``` method that will sort the list alphanumerically, ascending, by default:

    ```
    # Sort the list alphabetically:
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort()
    print(thislist)
    ```

    ```
    # Sort the list numerically:
    thislist = [100, 50, 65, 82, 23]
    thislist.sort()
    print(thislist)
    ```
    Sort Descending\n
    To sort descending, use the keyword argument ````reverse = True````:
    ```
    # Sort the list descending:
    thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
    thislist.sort(reverse = True)
    print(thislist)
    ```
    ```
    # Sort the list descending:
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse = True)
    print(thislist)
    ```
    Customize Sort Function\n
    You can also customize your own function by using the keyword argument ```key = function```.\n
    The function will return a number that will be used to sort the list (the lowest number first):\n
    ```
    # Sort the list based on how close the number is to 50:
    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key = myfunc)
    print(thislist)
    ```
    Case Insensitive Sort\n
    By default the ```sort()``` method is case sensitive, resulting in all capital letters being sorted before lower case letters:\n
    ```
    # Case sensitive sorting can give an unexpected result:
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort()
    print(thislist)
    ```
    Luckily we can use built-in functions as key functions when sorting a list.\n
    So if you want a case-insensitive sort function, use str.lower as a key function:\n
    ```
    # Perform a case-insensitive sort of the list:
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key = str.lower)
    print(thislist)
    ```
    Reverse Order\n
    What if you want to reverse the order of a list, regardless of the alphabet?\n
    The ```reverse()``` method reverses the current sorting order of the elements.\n
    ```
    # Reverse the order of the list items:
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.reverse()
    print(thislist)
    ```
    """

def m9_copy_list():
    """
    Copy a List
    You cannot copy a list simply by typing ```list2 = list1```, because: ```list2``` will only be a reference to ```list1```, and changes made in ```list1``` will automatically also be made in ```list2```.
    There are ways to make a copy, one way is to use the built-in List method ```copy()```.
    ```
    # Make a copy of a list with the copy() method:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
    ```
    Another way to make a copy is to use the built-in method ```list()```.
    ```
    # Make a copy of a list with the list() method:
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)
    ```
    """

def m10_join_two_list():
    """
    Join Two Lists\n
    There are several ways to join, or concatenate, two or more lists in Python.\n
    One of the easiest ways are by using the ```+``` operator.\n
    ```
    # Join two list:
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)
    ```
    Another way to join two lists are by appending all the items from list2 into list1, one by one:\n
    ```
    # Append list2 into list1:
    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]

    for x in list2:
        list1.append(x)

    print(list1)
    ```
    Or you can use the ```extend()``` method, which purpose is to add elements from one list to another list:\n
    ```
    # Use the extend() method to add list2 at the end of list1:
    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1)
    ```
    """

def m11_list_methods():
    """
    List Methods\n
    Python has a set of built-in methods that you can use on lists.\n

    ```
    # Method	Description
    append()	Adds an element at the end of the list
    clear()	Removes all the elements from the list
    copy()	Returns a copy of the list
    count()	Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	Sorts the list
    ```
    """
