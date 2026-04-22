# CHAPTER-1: BASICS (PRACTICE)
## Math Operations

print(2**5) # Exponentiation, Output: 32
### Exponentiation is right associative 
print(2 ** 3 ** 2) # Output: 512, because it is evaluated as 2 ** (3 ** 2) = 2 ** 9 = 512

print(23 % 7) # Modulus, Output: 2

print(30 // 4) # Floor Division, Output: 7

print(20 / 5) # Division, Output: 4.0 (always returns a float)

print(2 + 5) # Addition, Output: 7

print(31 - 23) # Subtraction, Output: 8

print(7 * 10) # Multiplication, Output: 70


##---------------------- Data Types(string, integer, float, Boolean) -----
name = "Sarah" # string
age = 18 # integer
height = 5.6 # float
is_student = True # Boolean

## --------------------- Variables -----
x = 10 # Assigning the value 10 to variable x
y = 5
print(x + y) # Output: 15

###----------------- Including variables in strings -----
name =  "Arwin" # Assigning the string "Arwin" to variable 'name'
print(name) # Output: Arwin
name = "Sarah"
print(name) # Output: Sarah, the previous value "Arwin" is overwritten

### ----------------- String concatenation and replication -----
name = "Sarah"
print("Hello," + " " + name + "!") # Output: Hello, Sarah!(string concatenation)
print("Hello,", name) # Output: Hello, Sarah (using comma in print adds a space automatically)
age = 18
print("18" * 3) # Output: 181818 (string replication)
print(age) # Output: 18

## --------------------- The type() function -----
weight = 56
print(type(weight)) # Output: <class 'int'>, weight is an integer
height = 5.6
print(type(height)) # Output: <class 'float'>, height is a float
language = "Python"
print(type(language)) # Output: <class 'str'>, language is a string

## --------------------- Type conversion (int(), float(), str()) -----
score = "70"
print(score + 10) # Output: TypeError, cannot concatenate str and int
print(int(score) + 10) # Output: 80, converts score to an integer before addition

print(score + str(10))  # Output: 7010, converts 10 to a string before concatenation

## --------------------- The round() and abs() functions -----
number = 2.5
print(round(number)) # Output: 2
print(round(4.6)) # Output: 5
 
print(abs(-5.4)) # Output: 5.4, (converts negative to positive)
print(abs(3.2)) # Output: 3.2, (positive number remains unchanged)


#                                           CHAPTER-2: CONTROL FLOW (PRACTICE)
## --------------------- Boolean Values (True and False) -----
is_running = True
is_walking = False 
print(is_running) # Output: True

## --------------------- Comparison Operators (==, !=, >, <, >=, <=) -----
my_age = 18
print(18 == 13) # Output: False, 18 is not equal to 13
print(18 == 18) # Output: True, 18 is equal to 18
print(my_age != 13) # Output: True, 18 is not equal to 13
print(my_age < 15) # Output: False, 18 is not less than 15
print(my_age > 15) # Output: True, 18 is greater than 15
print(my_age <= 18) # Output: True, 18 is less than or equal to 18
print(my_age >= 20) # Output: False, 18 is not greater than or equal to 20

## --------------------- Logical Operators (and, or, not) -----
is_sunny = True
is_cold = False
print(is_sunny and is_cold) # Output: False, both conditions must be true
print(is_sunny or is_cold) # Output: True, at least one condition is true
print(not is_sunny) # Output: False, negates the value of is_sunny


### ----------------- Mixing comparison and logical operators -----
x, y, z = 3, 7, 2
print(x < y and y > z) # Output: True, both conditions are true
print(x == 2 or y < z) # Output: False, neither condition is true


## --------------------- Components of flow control statements (if, elif, else) ---
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("Congratulations on reaching adulthood!")
else:
    print("You are an adult.")
# Output: Congratulations on reaching adulthood!, because age is equal to 18)

## --------------------- Nested if statements -----
number = 10
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
# Output: The number is positive. The number is even., because 10 is greater than 0 and is an even number.

## --------------------- Order of evaluating logical operators -----
print(True or False and False) # Output: True, because 'and' is evaluated before 'or'
print((True or False) and False) # Output: False, because the parentheses change the order of evaluation

print(True or False and not False and False) # Output: True, because 'not' is evaluated first, then 'and', and finally 'or'
# Step-by-step evaluation:
# 1. not False -> True
# 2. False and True -> False
# 3. False and False -> False
# 4. True or False -> True


# -------------------CODING CHALLENGE (write a program for age classifier)---
age = 18 
if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
elif 18 <= age < 65:
    print("You are an adult.")
else: 
    print("You are a senior citizen.")
# Output: You are an adult., because age is 18 which falls in the range of an adult (18 to 64).

num = 21 
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
# Output: Fizz, because 21 is divisible by 3 but not by 5.

## ------------------- CHAPTER-3 -------------------

# ----------- Understanding loops ------------

i = 0          # Q-1
while i < 3: 
    print(i)
    i = i + 1 
"""
Output :
0
1
2
"""
# Prints the old value of i before updating.

i = 0            # Q-2 
while i < 3:
    i = i + 1 
    print(i)
"""
Output:
1
2
3
"""
# Prints the new(updated) value of i after increment. 
# The order of statements inside the loop affects the output.

i = 0             # Q-3(infinite loop)
while i < 3:
    print(i)
# The loop keeps running forever and repeatedly prints 0, since the variable is never updated and the condtion i < 3 always remains True as i stays 0. 

# -------------- break and continue ----------

for i in range(5): # Q-4
    if i == 3:
        break
    print(i)
# break statement exits the loop and stops further iterations completely.

for i in range(5):  # Q-5
    if i == 3:
        continue
    print(i)
# When encountered continue statement skips the current iteration and moves to next iteration without executing the remaining code in the loop. 
# break ends the loop entirely, while continue only skips one iteration 

# ------------ range() understanding ----------

for i in range(2, 6): # Q-6
    print(i)

for i in range(1, 10, 3): # Q-7
    print(i)
"""
range(start, stop, step)
start : The number from which the loop begins.
stop : The number at which the loop stops(not included)
step : The increment between the values
"""

# -------------- Truthy / Falsey --------------

if "":            # Q-8
    print("A")
else:
    print("B")

print(bool(" "))   # Q-9
print(bool(""))

"""
Note:
In python some values are considered False in conditions(Falsey values):
Falsey values: 0, 0.0, an empty string, None
- All the other values are considere True(Truthy values)
"""

# ------------- Convert for loop into a while loop ----------

for i in range(3):  # Q-10
    print(i)
"""
Equivalent while loop 
i = 0
while i < 3:
    print(i)
    i = i + 1
"""
