"""
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```
Dictionary\n
Dictionaries are used to store data values in key:value pairs.\n

A dictionary is a collection which is unordered, changeable and does not allow duplicates.\n

Dictionaries are written with curly brackets, and have keys and values:\n

```
# Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
```
"""

def m0_dictionary_properties():
    """
    Dictionary Items\n
    Dictionary items are unordered, changeable, and does not allow duplicates.\n

    Dictionary items are presented in key:value pairs, and can be referred to by using the key name.\n

    ```
    # Print the "brand" value of the dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict["brand"])
    ```
    Unordered\n
    When we say that dictionaries are unordered, it means that the items does not have a defined order, you cannot refer to an item by using an index.\n

    Changeable\n
    Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.\n

    Duplicates Not Allowed\n
    Dictionaries cannot have two items with the same key:\n

    ```
    # Duplicate values will overwrite existing values:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
    }
    print(thisdict)
    ```
    Dictionary Length\n
    To determine how many items a dictionary has, use the len() function:\n

    ```
    # Print the number of items in the dictionary:

    print(len(thisdict))
    ```
    Dictionary Items - Data Types\n
    The values in dictionary items can be of any data type:\n

    ```
    # String, int, boolean, and list data types:

    thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
    }
    ```
    ```type()```\n
    From Python's perspective, dictionaries are defined as objects with the data type 'dict':\n

    ```
    <class 'dict'>
    ```
    ```
    # Print the data type of a dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(type(thisdict))
    ```
    """

def m1_access_dictionary_items():
    """
    Accessing Items\n
    You can access the items of a dictionary by referring to its key name, inside square brackets:\n

    ```
    # Get the value of the "model" key:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    x = thisdict["model"]
    ```
    There is also a method called get() that will give you the same result:\n

    ```
    # Get the value of the "model" key:

    x = thisdict.get("model")
    ```
    Get Keys\n
    The ```keys()``` method will return a list of all the keys in the dictionary.\n

    ```
    # Get a list of the keys:

    x = thisdict.keys()
    ```
    The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.\n

    ```
    # Add a new item to the original dictionary, and see that the value list gets updated as well:

    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    x = car.keys()

    print(x) #before the change

    car["color"] = "white"

    print(x) #after the change
    ```
    Get Values\n
    The ```values()``` method will return a list of all the values in the dictionary.\n

    ```
    # Get a list of the values:

    x = thisdict.values()
    ```
    The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.\n

    ```
    # Add a new item to the original dictionary, and see that the keys list gets updated as well:

    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    x = car.values()

    print(x) #before the change

    car["year"] = 2020

    print(x) #after the change
    ```
    Get Items\n
    The ```items()``` method will return each item in a dictionary, as tuples in a list.\n

    ```
    # Get a list of the key:value pairs

    x = thisdict.items()
    ```
    The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.\n

    ```
    # Add a new item to the original dictionary, and see that the items list gets updated as well:

    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    x = car.items()

    print(x) #before the change

    car["year"] = 2020

    print(x) #after the change
    ```
    Check if Key Exists\n
    To determine if a specified key is present in a dictionary use the in keyword:\n

    ```
    # Check if "model" is present in the dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    ```
    """

def m2_change_dictionary_items():
    """
    Change Values\n
    You can change the value of a specific item by referring to its key name:\n

    ```
    # Change the "year" to 2018:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["year"] = 2018
    ```
    Update Dictionary\n
    The ```update()``` method will update the dictionary with the items from the given argument.\n

    The argument must be a dictionary, or an iterable object with ```key:value``` pairs.\n

    ```
    # Update the "year" of the car by using the update() method:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.update({"year": 2020})
    ```
    """

def m3_add_dictionary_items():
    """
    Adding Items\n
    Adding an item to the dictionary is done by using a new index key and assigning a value to it:\n

    ```
    # thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)
    ```
    Update Dictionary\n
    The ```update()``` method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.\n

    The argument must be a dictionary, or an iterable object with ```key:value``` pairs.\n

    ```
    # Add a color item to the dictionary by using the update() method:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.update({"color": "red"})
    ```
    """

def m4_remove_dictionary_items():
    """
    Removing Items\n
    There are several methods to remove items from a dictionary:\n

    ```
    # The pop() method removes the item with the specified key name:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)
    # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.popitem()
    print(thisdict)
    # The del keyword removes the item with the specified key name:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    del thisdict["model"]
    print(thisdict)
    # The del keyword can also delete the dictionary completely:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    del thisdict
    print(thisdict) #this will cause an error because "thisdict" no longer exists.
    # The clear() method empties the dictionary:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.clear()
    print(thisdict)
    ```
    """

def m5_loop_through_dictionary_items():
    """
    Loop Through a Dictionary\n
    You can loop through a dictionary by using a for loop.\n

    When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.\n

    ```
    # Print all key names in the dictionary, one by one:

    for x in thisdict:
        print(x)
    # Print all values in the dictionary, one by one:

    for x in thisdict:
        print(thisdict[x])
    # You can also use the values() method to return values of a dictionary:

    for x in thisdict.values():
        print(x)
    # You can use the keys() method to return the keys of a dictionary:

    for x in thisdict.keys():
        print(x)
    # Loop through both keys and values, by using the items() method:

    for x, y in thisdict.items():
        print(x, y)
    ```
    """

def m6_copy_dictionaries():
    """
    Copy a Dictionary\n
    You cannot copy a dictionary simply by typing ```dict2 = dict1```, because: ```dict2``` will only be a reference to ```dict1```, and changes made in ```dict1``` will automatically also be made in ```dict2```.\n

    There are ways to make a copy, one way is to use the built-in Dictionary method ```copy()```.\n

    ```
    # Make a copy of a dictionary with the copy() method:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)
    ```
    Another way to make a copy is to use the built-in function ```dict()```.\n

    ```
    # Make a copy of a dictionary with the dict() function:

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    mydict = dict(thisdict)
    print(mydict)
    ```
    """

def m7_nested_dictionaries():
    """
    Nested Dictionaries\n
    A dictionary can contain dictionaries, this is called nested dictionaries.\n

    ```
    # Create a dictionary that contain three dictionaries:

    myfamily = {
        "child1" : {
            "name" : "Emil",
            "year" : 2004
        },
        "child2" : {
            "name" : "Tobias",
            "year" : 2007
        },
        "child3" : {
            "name" : "Linus",
            "year" : 2011
        }
    }
    ```
    Or, if you want to add three dictionaries into a new dictionary:\n

    ``
    `# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

    child1 = {
    "name" : "Emil",
    "year" : 2004
    }
    child2 = {
    "name" : "Tobias",
    "year" : 2007
    }
    child3 = {
    "name" : "Linus",
    "year" : 2011
    }

    myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }
    ```
    """

def m8_dictionary_methods():
    """
    Dictionary Methods\n
    Python has a set of built-in methods that you can use on dictionaries.\n

    ```
    # Method	Description
    clear()	Removes all the elements from the dictionary
    copy()	Returns a copy of the dictionary
    fromkeys()	Returns a dictionary with the specified keys and value
    get()	Returns the value of the specified key
    items()	Returns a list containing a tuple for each key value pair
    keys()	Returns a list containing the dictionary's keys
    pop()	Removes the element with the specified key
    popitem()	Removes the last inserted key-value pair
    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    update()	Updates the dictionary with the specified key-value pairs
    values()	Returns a list of all the values in the dictionary
    ```
    """