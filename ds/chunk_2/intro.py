"""
Scala Type\n
1. Booleans\n
2. Numbers\n
3. Casting\n
4. String\n
5. Operators\n

# Booleans\n
Booleans represent one of two values: ```True``` or ```False```.\n
When you compare two values, the expression is evaluated and Python returns the Boolean answer:\n
```
print(10 > 9)
print(10 >= 9)
print(10 == 9)
print(10 < 9)
print(10 <= 9)
```
Evaluate a string and a number:\n
```
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```
Almost any value is evaluated to True if it has some sort of content.\n
Any string is True, except empty strings.\n
Any number is True, except 0.\n
Any list, tuple, set, and dictionary are True, except empty ones.\n
The following will return False:\n
```
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
```
Python also has many built-in functions that return a boolean value, like the ```isinstance()``` function, which can be used to determine if an object is of a certain data type:\n
```
x = 200
print(isinstance(x, int))
```
# Numbers\n
There are three numeric types in Python:\n
```int```\n
```float```\n
```complex```\n
Variables of numeric types are created when you assign a value to them:\n
```
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```
To verify the type of any object in Python, use the type() function:\n
```
print(type(x))
print(type(y))
print(type(z))
```

Integers:\n
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.\n
```
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

Floats:\n
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.\n
```
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```
Float can also be scientific numbers with an "e" to indicate the power of 10.\n
```
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```
Complex:\n
Complex numbers are written with a "j" as the imaginary part:\n
```
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```
You can convert from one type to another with the int(), float(), and complex() methods:\n
```
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```
# Casting
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.\n

Casting in python is therefore done using constructor functions:\n
    int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)\n
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)\n
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals\n
Integers:\n
```
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```
Floats:\n
```
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```
Strings:\n
```
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```
# Strings\n
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".\n
You can display a string literal with the print() function:\n
```
print("Hello")
print('Hello')
```
# Operators\n
Operators are used to perform operations on variables and values.\n
In the example below, we use the ```+``` operator to add together two values:\n
```
print(10 + 5)
```
Python divides the operators in the following groups:\n
    Arithmetic operators\n
    Assignment operators\n
    Comparison operators\n
    Logical operators\n
    Identity operators\n
    Membership operators\n
    Bitwise operators\n
Arithmetic operators are used with numeric values to perform common mathematical operations:\n
```
Operator	Name	Example
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus	x % y
**	Exponentiation	x ** y
//	Floor division	x // y
```
Assignment operators are used to assign values to variables:\n
```
Operator	Example	Same As
=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
//=	x //= 3	x = x // 3
**=	x **= 3	x = x ** 3
&=	x &= 3	x = x & 3
|=	x |= 3	x = x | 3
^=	x ^= 3	x = x ^ 3
>>=	x >>= 3	x = x >> 3
<<=	x <<= 3	x = x << 3
```
Comparison operators are used to compare two values:\n
```
Operator	Name				Example
==		Equal				x == y
!=		Not equal			x != y
>		Greater than			x > y
<		Less than			x < y
>=		Greater than or equal to	x >= y
<=		Less than or equal to		x <= y
```
Logical operators are used to combine conditional statements:\n
```
Operator	Description				Example
and 	Returns True if both statements are true			x < 5 and  x < 10
or		Returns True if one of the statements is true			x < 5 or x < 4
not		Reverse the result, returns False if the result is true		not(x < 5 and x < 10)
```
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:\n
```
Operator	Description	Example
is 		Returns True if both variables are the same object	x is y
is not	Returns True if both variables are not the same object	x is not y
```
Membership operators are used to test if a sequence is presented in an object:\n
```
Operator	Description 					Example
in 		Returns True if a sequence with the specified value is present in the object		x in y
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
```
Bitwise operators are used to compare (binary) numbers:

```
Operator	Name		Description
& 	AND			Sets each bit to 1 if both bits are 1
|	OR			Sets each bit to 1 if one of two bits is 1
^	XOR			Sets each bit to 1 if only one of two bits is 1
~	NOT			Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
```
"""
