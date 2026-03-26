* Use backticks (`) to represent code (variables, functions, examples).
* Use code blocks (```python) for multi-line code.

# CHAPTER ONE 
---
## MATH OPERATORS IN PYTHON 
---
### 1. Exponentiation ( ** ) 
 x**y , this means x raised to the power of y . 
 Example: `print(5**2)`
 Output : `25`

### 2. Modulus/remainder ( % ) 
 x % y , this gives the remainder when x is divided by y .
 Example: `print(10 % 3)`
 Output : `1`

### 3. Integer division ( // ) 
Integer division is same as the regular division but the result is rounded down .
Example: `print(9 // 2)`
Output : `4`
* Since we are using rounding down which means moving towards the smaller number .

### 4. Division ( / ) 
This division gives floating point number .  
Example: `print(7 / 2)`

### 5. Other arithmetic operators 
`*` -> Multiplication 
`+` -> addition
`-` -> subtraction 
---
## DATA TYPES
* The most common data types in python are 

### 1. Integer (int):
* Whole numbers without fractions . 
ex : 10 , -3 , 0 .

### 2. Floating-point number (float):
* Represents numbers with decimal points .
ex : 3.5 

### 3. String (str):
* Represents a sequence of characters written inside quotes (either single , double , triple etc) . 
- It can include letters , numbers , symbols and spaces . 
Example: `name = "Hello"`
- THE len() function , is used to evaluate the number of characters in that string .
Example : `print(len('hello'))`
Output : `5`
- Integer, floating point and string aren't the only data types in python . 
---
 ### Finding data types
* Use `type()` to find the data type.
Example : `print(type("3"))`
Output: `<class 'str'> `

## STRING CONCATENATION AND REPLICATION 
- '+' operator is used to combine 2 string values .
- '+' is the concatenation operator .
Example : `print("Hi" + "Hello")`
Output : `HiHello`
---
- '*' repeats the string multiple times. 
- '*' is the string replication operator.
Example : `print("Hi" * 3)`
Output : `HiHiHi`
## THE str(), int(), float() functions 
- To concatenate an integer with string , you will have to change the integer to a string using str()

1. Example : 
```python
x = 13 , y = '12'
print(str(x) + y)
```
Output : `1312`

2. Example : 
```python 
print(x + int(y))
```
Output : `25`

---
## VARIABLES
- A variable is like a box in the computer memory where you can store data and manipulate it (change) .
Example : 
```python
x = 10 
print(x)
``` 
Output : `10`

---
### OVERWRITING THE VARIABLE
- A variable is created when a value is first assigned .
- Assigning a new value replaces the old value , this is called " OVERWRITING THE VARIABLE " . 
Example : 
```python
x = 12 
x = 15 
print(x)
```
Output : `15`

---
### VARIABLE NAMES (Rules)
1. Cannot contain spaces .
Example : current balance (instead of space we use an underscore)
2. It can use only letters , numbers, and the underscore . 
ex : current_balance , account2 , etc .
3. It cannot start with a number . 
ex : 42 is wrong , _42 is right 
- Variables can start with underscore . eg: _43
4. Cannot use python keywords . (like if , for , return)
5. In python it is a convention to start variable with a lowercase letter.
6. Python is case sensitive , meaning it treats uppercase and lowercase letters as different.
Example : 
```python
age = 15
Age = 20
print(age)
print(Age)
```
Output : 
```python
15
20
```
* `age` and `Age` are different variables . 

---
## COMMENTS
- # is used to write comments .
- Python ignores comments .
Example : 
```python
# print("Hello")
```
### COMMENTING OUT CODE 
- Sometimes we put a hash mark(#) in front of a line of code to temporarily remove it while testing a program . 
---
## THE print() FUNCTION 
- The print() function displays the stirng value inside the parantheses on the screen : 
Example : 
```python
print('Hello, World!')
```
Output : `Hello, World!`
- A value that is passed to a function call is an argument. 
* (In the above example 'Hello, World!' is the argument passed to the print() function.)
---
## TEXT AND NUMBER EQUIVALANCE 
- Example : `23 == '23'`
Output : `False`
- Example : `23 == 23.000`
Output : `True`
- This is because strings are text , while integers and floats are numbers . 
---
## THE type() FUNCTION 
- Use type() function to determine what type they are . 
Example : 
`print(type('forty two'))`
Output : ` <class 'str'>

---
## THE round() and abs() FUNCTION
- These python functions are like the len()function, take an argument and return a value. 
### 1. The round() function
- Accepts a float value and returns the nearest integer . 
Example : `print(round(-2.23))`
Output : -2

- For numbers that end with .5 the number is rounded to the nearest even integer.(" This is called banker's rounding ")
Example : `print(round(6.5))`
Output : `6`

### The abs() function
- Returns the absolute value (distance from 0 on a number line) of a number. 
- It converts negative numbers to positive and leaves positive numbers and zero unchanged.
Example : `print(abs(-1.59))`
Output : `1.59`
Example : `print(abs(23))`
Output : `23` 

---
## EXPRESSION
- An expression is a combination of values and operators. All expressions evaluate (that is, reduce) to a single value.

## Difference between statement and expression
- An expression evaluates to a single value. A statement does not.
