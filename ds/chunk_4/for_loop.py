"""
# Python ```for``` Loops\n
A ```for``` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).\n

This is less like the ```for``` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.\n

With the ```for``` loop we can execute a set of statements, once for each item in a list, tuple, set etc.\n

```
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
The ```for``` loop does not require an indexing variable to set beforehand.\n

# Looping Through a ```string```\n
Even strings are iterable objects, they contain a sequence of characters:\n

```
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)
```
# The ```break``` Statement\n
With the ```break``` statement we can stop the loop before it has looped through all the items:\n

```
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```
```
# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
```
# The ```continue``` Statement\n
With the ```continue``` statement we can stop the current iteration of the loop, and continue with the next:\n

```
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```
# The ```range()``` Function\n
To loop through a set of code a specified number of times, we can use the ```range()``` function,
The ```range()``` function returns a sequence of numbers, starting from 0 by default, and increments by ```1``` (by default), and ends at a specified number.\n

```
# Using the range() function:

for x in range(6):
  print(x)
```
Note that ```range(6)``` is not the values of ```0``` to ```6```, but the values ```0``` to ```5```.\n

The ```range()``` function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:``` range(2, 6)```, which means values from 2 to 6 (but not including 6):\n

```
# Using the start parameter:

for x in range(2, 6):
  print(x)
```
The ```range()``` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: ```range(2, 30, 3)```:\n

```
# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
```
# ```Else``` in For Loop\n
The ```else``` keyword in a for loop specifies a block of code to be executed when the loop is finished:\n

```
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
Note: The ```else``` block will NOT be executed if the loop is stopped by a ```break``` statement.\n

```
# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
```
# Nested Loops\n
A nested loop is a loop inside a loop.\n

The "inner loop" will be executed one time for each iteration of the "outer loop":\n

```
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```
# The ```pass``` Statement\n
```for``` loops cannot be empty, but if you for some reason have a ```for``` loop with no content, put in the ```pass``` statement to avoid getting an error.\n

```
for x in [0, 1, 2]:
  pass
```
"""
