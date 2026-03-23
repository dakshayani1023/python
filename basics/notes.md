* Use backticks (`) to represent code (variables, functions, examples).
* Use code blocks (```python) for multi-line code.

## MATH OPERATORS IN PYTHON 
---
### 1. Exponentiation ( ** ) 
 x**y , this means x raised to the power of y . 
 Example: `print(5**2)`

### 2. Modulus/remainder ( % ) 
 x % y , this gives the remainder when x is divided by y .
 Example: `print(10 % 3)`

### 3. Integer division ( // ) 
Integer division is same as the regular division but the result is rounded down .
Example: `print(9 // 2)`

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