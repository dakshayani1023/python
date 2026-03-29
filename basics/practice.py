# CHAPTER-1: BASICS

# 1. Variables and Data Type
# Exercises
# 1. Create a variable called 'name' and assign it your name. Then print the variable.
name = 'Dakshayani'
print(name) # Output : Dskshayani

# 2. Create a variable called 'age' and assign it your age. Then print the variable.
age = 18
print(age) # Output : 18

# 3. Create a variable called 'is_student' and assign it a boolean value indicating whether you are a student or not. Then print the variable.
is_student = True 
print(is_student) # Output : True

# 2.Data Types
# Exercise
# 1. Create a variable called 'pi' and assign it the value of 3.14. Then print the variable.
pi = 3.14
print(pi) # Output : 3.14

# ------------------- A Short Program : Dishonest Capacity Calculator -------------------

print('Enter TB or GB for the advertised unit:')
unit = input('>')
# Calculate the amount that the advertised capacity lies:
if unit == 'TB':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

real_capacity = str(round(advertised_capacity * discrepancy, 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)