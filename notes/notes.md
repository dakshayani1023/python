* Use backticks (`) to represent code (variables, functions, examples).
* Use code blocks (```python``` ) for multi-line code.

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
* This is also called 'Floor Division'.
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
x , y = 13 , '12' 
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
2. It can use only letters , numbers. 
ex : current_balance , account2 , etc .
3. It cannot start with a number . 
ex : 42 is wrong , _42 is right 
- Variables can start with underscore . eg: _43
4. Cannot use python keywords . (like if , for , return)
5. In python it is a convention to start variable with a lowercase letter.
---
### NOTE 
- Python is case sensitive , meaning it treats uppercase and lowercase letters as different.
Example : 
```python
age = 15
aGe = 20
print(age)
print(aGe)
```
Output : 
```python
15
20
```
* `age` and `aGe` are different variables . 

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
- The print() function displays the string value inside the parentheses on the screen : 
Example : 
```python
print('Hello, World!')
```
Output : `Hello, World!`
- A value that is passed to a function call is an argument. 
* (In the above example 'Hello, World!' is the argument passed to the print() function.)
---
## TEXT AND NUMBER EQUIVALANCE 
- Example : `print(23 == '23')`
Output : `False`
- Example : `print(23 == 23.000)`
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
## BOOLEAN OPERATORS or LOGICAL OPERATORS
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
- ` The order of evaluating the Boolean operators is: 1. not operators, 2. and operators, 3. or operators

Example : 
``` python
spam = 6
print(3 + 3 == spam and not 3 + 3 == spam + 1)
```
Output : `True`
Explanation : Here not 3 + 3 == spam + 1 means "Is it True that (3+3) is not equal to (spam+1)" and the Boolean value on the either sides of and is True the final output is True.

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
       print("my_age")  -> indentation decreased → block already ended → now outside and will execute regardless of the statement(since it is outside the block.)

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
    print("A")          # inside that block

print("B")              # block ended (back to 0)

if True:                # new block starts again
    print("C")
```

---
## FLOW CONTROL STATEMENTS 
### 1. if statement
- It is the most common type of flow control statement.
- An if statement's clause will execute if the statement's condition is True.
- The clause is skipped if the condition is False.
* CLAUSE : It is the block following the if statement.

- In python, an if statement conists
1. The if keyword.
2. A condition (an expressin that evaluates to True or False)
3. A colon(:)
4. Starting the next line after the condition with an indented block of code (called the if clause or if block)
Example : 
```python
name = 'Addison'
if name == 'Addison':
   print('Hi, Addison.')
```
Output : `Hi, Addison`

---
### 2. else statement
- The else clause is executed only when the if statement is False.
- else statement never has a condition.
- An else statement always consists of :
1. The else keyword
2. A colon
3. Starting the next line after the condition with an indented block of code(called the else clause or else block)
Example: 
```python
name = 'Chloe'
if name == 'Emma':
   print('Hi, Emma')
else:
   print('Hello, stranger')
```
Output : `Hello, stranger`

---
### 3. elif statement (else if)
- We use if or else when you want only one of the clauses to execute.
- An elif statement is used to check multiple conditions sequentially after an initial if statement.

### HOW elif WORKS
1. Python checks the initial if condition first.
2. If the if condition is False, Python moves to the first elif condition and evaluates it and this process continues until the condition is found.
3. Once a condition is met, the programs skips all remaning elif and else conditions.
4. If none of the if and elif conditions are True, the optional else block at the end will be executed.
Example :
```python
age = 25
if age < 18:
   print("You are a minor.")
elif age >= 18 and age < 65:   
   print("You are an adult.")
else:
   print("Your are a senior citizen.")
```
Output : `You are an adult.`
---
### Example:
```python
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.') # Check the most specific/extreme case first
elif age > 2000:
   print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:  # This will only be checked if age is NOT over 2000
    print('You are not Alice, grannie.')
elif age < 12:
    print('You are not Alice, kiddo.')
```
Output : `Unlike you, Alice is not an undead, immortal vampire.`
---
### NOTE
- A quick rule:
1. When using >(greater than), start with the highest number and work your way down.
2. When using <(less than), start with the lowest number and work your way down.
 
#  ------------------- CHAPTER-3 (LOOPS) -------
- Python has 2 kinds of loops, 'while' and 'for'. 
## 1. while Loop Statements 
- A block of code is executed over and over again using a while loop statement. 
- The code in a while clause is executed as long as the statement's condition is True.

## HOW while LOOP WORKS (IMPORTANT)
* A while loop runs as long as the condition is True.
* The loop does NOT run everything at once.
* It runs step-by-step (line by line) for each iteration.
## EXECUTION FLOW
For every iteration:
1. Check the condition
2. If True → enter the loop
3. Execute all lines inside the loop from top to bottom
4. Go back and check the condition again.

## Loop Control Variable 
- A variable used in the condition controls when the loop stops.
- It must be updated inside the loop.
- If not updated --> infinite loop (loop runs forever)
Example for while loop: 
```python
z = 1 
while z < 7: 
   print(z)
   z = z + 1
``` 
Output : 1
         2
         3
         4
         5
         6

## Infinite loop: 
- If the condition never becomes false, the loop runs forever.
Ex: 
```python
x = 0 
while x < 5:
   print(x) 
```
(In the above example - x is never updated -> Infinite loop)

## break Statements
- To get the program execution break out of a while's loop clause early we use a break statement.
- A break statement simply contains the keyword break.
- The loop stops when the program reaches the keyword break.
Example:
```python
while True:
   print("What is your name?")
   name = input()
   if name == "Audrey":
       break # Indented further because it's inside the 'if' block
print("Hi Audrey!, Nice to meet you.")
``` 
Explanation:
1. Since we already used while true, the loop will never stop on it's own.
2. The break is the only way out.
3. If name == "Audrey" is False. Python ignores the break and goes back to the top of the loop to ask the question again.
4. If name == "Audrey" is True. Python hits the break, jumps out of the loop immediately and prints the "Nice to meet you."message.

Example:
```python
while True:
    print(" Hi! My name is Leah.")
    break 
    print(" This will never run.") 
```
Output: Hi! My name is Leah. 


## NOTE
### TRAPPED IN AN INFINITE LOOP?
- If you ever run a program that has bug causing it to get stuck in an infinite loop, press ctrl-c; this will send a keyboardInterrupt error to your program and cause it to stop immediately. 
Example: 
```python
while True:
   print("Hello, world!")
```
Output: The above line of code will keep printing Hello, world! until you press ctrl-c.


## continue Statements 
- When the program execution reaches a continue statement, it jumps back to the start of the loop and reevaluates the loop's condition. 

## TRUTHY and FALSEY values and the BOOL() function
- When used in conditions 0, 0.0, ''(empty string without a space), [](empty list),None are considered False.
- All the other values (ex: ' ', any integer, " ",etc) are considered True.

Example: 
```python
name = ''
while not name:
   print('Enter your name':)
   name = input()
```
Explanation: 
name = ''
- An empty string ('') is considered False in Python.

- Condition:
while not name

- Step-by-step:
bool(name) → False  (when you print bool(name) the output will be False.)
not False → True  

- So, the condition becomes True and the loop runs.

- The program prints "Enter your name" and waits for user input.

---

## for Loops and the range() Function
- To execute a block of code certain no.of times we use a for loop statement and the range() function.

### NOTE:
- We can only use continue and break statements inside while and for loops only.

---

## An Equivalent while Loop
- We can actually use a while loop to do the same thing as a for loop.(for loops are just more concise.)
Example: 
```python
print('Hello!')
i = 0
while i < 3:
   print('On this iteration, i is set to ' + str(i))
   i = i + 1 
print('Goodbye!')
```
---

## Arguments to range()
- Some functions can be called with multiple arguments seperated by a comma and range is one of them.
- The range() function can be interpreted differently depending on whether you pass one, two, or three arguments.
--> range(stop), range(start, stop), range(start, stop, step) (simialr to slicing)

---

## Importing Modules

### WHAT IS A MODULE?
- A module is a Python file that contains pre-written code such as functions, variables, and classes that you can use in your program.
Example: For 
1. Random numbers --> use a module
2. Math calculations --> use a module

- Each module contains a related group of functions and other code that can be reused in different programs.
- Before using a  module, you must import it using an import statement.

### IMPORT STATEMENT
An import statement consists of:
1. The import keyword
2. The name of the module
3. Optionally, multiple module names seperated by commas
ex: import math, random

### HOW TO IMPORT A MODULE
- Basic syntax : import module_name
Example: 
```python
import random   
print(random.randint(1,10))
```
Output: Random number between 1 and 10
- random = module & randint() = function inside that module

### NOTE: 
- Instead of importing everything, use:
```python
from random import randint 
print(randint(1,10))
```
- Now we don't need to write random again.

### SIMPLE WAY TO REMEMBER
- Module = Library
- Import = Entering the library
- Function = Picking a book 
