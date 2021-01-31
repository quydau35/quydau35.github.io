"""
# Python Classes/Objects\n
Python is an object oriented programming language.\n

Almost everything in Python is an object, with its properties and methods.\n

A Class is like an object constructor, or a "blueprint" for creating objects.\n

# Create a Class\n
To create a class, use the keyword class:\n

```
# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
```
# Create Object\n
Now we can use the class named MyClass to create objects:\n

```
# Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)
```
# The ```__init__()``` Function\n
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.\n

To understand the meaning of classes we have to understand the built-in ```__init__()``` function.\n

All classes have a function called ```__init__()```, which is always executed when the class is being initiated.\n

Use the ```__init__()``` function to assign values to object properties, or other operations that are necessary to do when the object is being created:\n

```
# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
```
Note: The ```__init__()``` function is called automatically every time the class is being used to create a new object.\n

# Object Methods\n
Objects can also contain methods. Methods in objects are functions that belong to the object.\n

Let us create a method in the Person class:\n

```
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
```
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.\n

# The ```self``` Parameter\n
The ```self``` parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.\n

It does not have to be named ```self```, you can call it whatever you like, but it has to be the first parameter of any function in the class:\n

```
# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```
# Modify Object Properties\n
You can modify properties on objects like this:\n

```
# Set the age of p1 to 40:

p1.age = 40
```
# Delete Object Properties\n
You can delete properties on objects by using the del keyword:\n

```
# Delete the age property from the p1 object:

del p1.age
```
# Delete Objects\n
You can delete objects by using the del keyword:\n

```
# Delete the p1 object:

del p1
```
# The pass Statement\n
```class``` definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.\n

```
class Person:
    pass
```

# Python Inheritance\n
Inheritance allows us to define a class that inherits all the methods and properties from another class.\n

```Parent class``` is the class being inherited from, also called base class.\n

```Child class``` is the class that inherits from another class, also called derived class.\n
Create a Parent Class\n
Any class can be a parent class, so the syntax is the same as creating any other class:\n

```
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()
```
# Create a Child Class\n
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:\n

```
# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
    pass
```
Note: Use the pass keyword when you do not want to add any other properties or methods to the class.\n

Now the Student class has the same properties and methods as the Person class.\n

```
# Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()
```
# Add the ```__init__()``` Function\n
So far we have created a child class that inherits the properties and methods from its parent.\n

We want to add the ```__init__()``` function to the child class (instead of the pass keyword).\n

Note: The ```__init__()``` function is called automatically every time the class is being used to create a new object.\n

```
# Add the __init__() function to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        #add properties etc.
```
When you add the ```__init__()``` function, the child class will no longer inherit the parent's ```__init__()``` function.\n

Note: The child's ```__init__()``` function overrides the inheritance of the parent's ```__init__()``` function.\n

To keep the inheritance of the parent's ```__init__()``` function, add a call to the parent's ```__init__()``` function:\n

```
# class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
```
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the ``__init__()`` function.\n

# Use the ```super()``` Function\n
Python also has a ```super()``` function that will make the child class inherit all the methods and properties from its parent:\n

```
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```
By using the ```super()``` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.\n

# Add Properties\n
```
# Add a property called graduationyear to the Student class:

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
```
In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the ```__init__()``` function:\n

```
# Add a year parameter, and pass the correct year when creating objects:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
```
# Add Methods\n
```
# Add a method called welcome to the Student class:

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```
If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.\n
"""