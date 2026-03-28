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

---
# ----------------------CHAPTER-2----------------------------
## BOOLEAN VALUES 
- Boolean data type has only two values:True and False .
- Boolean values can be stored in variables.
Example :
```python
light = True 
print(light)
```
Output: `True`
- We cannot use True and False for variable names.

---
## COMPARISION OPERATORS
- They are also called relational operators.
- They compare two values and evaluate down to a single Boolean value.(either True or False)
## OPERATORS 
1. Equal to(==):
2. Not equal to(!=): 
3. Less than(<): 
4. Greater than(>): 
5. Less than or equal to(<=):
6. Greater than or equal to(>=)
- We often use comparision operators to compare a variable's value to some other value.
Example : 
``` python
my_age = 18
print(my_age > 20)
```
Output : `False`

--- 
## NOTE:THE DIFFERENCE BETWEEN THE == AND = OPERATORS
- The == (equal to) operator asks whether two values are the same as each other.
- The = (assignment) operator puts the value on the right into the variable on the left.

---
## BOOLEAN OPERATORS 
- The 3 Boolean operators(and, or, and not) operate on Boolean values(or expressions that result in Boolean values).
---
## 1.and OPERATOR
- The and operator always takes 2 Boolean values(or expressions), so it is considered as a binary Boolean operator. 
   * It evaluates an expression to True if both values are true otherwise, it evaluates to False.
### THE and OPERATOR'S TRUTH TABLE
- True and True   -> True
- True and False  -> False
- False and False -> False
- False and True  -> False
--- 
## 2. or OPERATOR
- This is also a binary Boolean operator.
- This operator evaluates the value to True if either of the Boolean values is True.
### THE or OPERATOR'S TRUTH TABLE
- True or True   -> True
- True or False  -> True
- False or True  -> True
- False or False -> False
---
## 3. not OPERATOR 
- The not operator evaluates to the opposite Boolean value .
- The operator operates on only one Boolean value, so it is a unary operator.
### THE not OPERATOR'S TRUTH TABLE
- not True  -> False 
- not False -> True 
---
## MIXING BOOLEAN AND COMPARISION OPERATORS 
- Since comparision operators evaluate to Boolean values, you can use them in expressions with Boolean operators.
Example : 
```python
x,y,z = 12,14,15
print(x < y and y > z)
```
Output : `False`

- The computer will evaluate the left expression first, then it will evaluate the right expression.(x < y is evaluated first then y > z is evaluated in the above example.)
- ` The order of evaluating the Boolean operators is not operators first, then the and operators, and then the or operators.`
Example : 
``` python
spam = 6
print(3 + 3 == spam and not 3 + 3 == spam + 1)
```
Output : `True`
Explanation : Here not 3 + 3 == spam + 1 means "Is it True that (3+3) is not equal to (spam+1) and the Boolean value on the either sides of and is True the final output is True.

---
## COMPONENTS OF FLOW CONTROL
- Flow control statements start with a part called the condition and are followed by block of code called the clause.

### CONDITIONS
- Conditions are similar to expressions since a condition always evaluates to a Boolean value(True or False)
- Almost every flow control statement uses a condition.

### BLOCKS OF CODE
- Lines of python code grouped together in blocks.
- Based on the indentation(means 4 spaces or a tab) of the lines of code, you can tell when a block begins and ends.
### FOUR RULES FOR BLOCKS: 
1. A new block begins when the indentation increases.
Example :
```python
if True:
   print("Hello")
```
- In the above example if True: -> starts a block
and the indented line(print)  -> belongs inside that block.

2. Blocks can contain other blocks
Example: 
```python
if True:               # ground floor
   print("Level 1")    # first floor
   if True:            # first floor
      print("Level 2") # second floor
```
- Here first if  -> outer block or the first block
       second if -> inside the first block      
       
3. A block ends when indentation decreases.
Example:
```python
if True:
   print("my_name")
print("my_age")
```
- Here print("my_name") -> inside if
       print("my_age")  -> indentation decreased → block already ended → now outside

4. Python expects a block after a colon(:)
- That means whenever we write a statement ending with : python expets an indented block next.(common statements if,for, while etc)
Example:
```python
if True:
   print("Hello")
```
---

### NOTE
1. The line with : (like if True:) → starts a block
2. Indented lines → inside that block
3. When indentation goes back to 0 → block ends
4. Now you are outside the block
5. If you want another block → you must start it again with :
EXAMPLE FOR THE ABOVE STEPS:
```python
if True:                # block starts
    print("A")          # inside block

print("B")              # block ended (back to 0)

if True:                # new block starts again
    print("C")
```

---