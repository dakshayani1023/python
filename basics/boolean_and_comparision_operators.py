# Boolean Values
spam = True
print(spam) # Output : True

# Comparision Operators 
x = 42
y = 42 
print(x == y) # Output : True

x,y = 2,2
print(x != y) # Output : False

x = 'Hello'
y = 'hello'
print(x != y) # Output : True 

x,y = 42,42.0
print(x == y) # Output : True

x,y = 100,42
print(x < y) # Output : False

eggs = 23
print(eggs <= 23) # Output : True
print(eggs < 23) # Output : False
print(eggs > 23) # Output : False
print(eggs >= 23) # Output : True

my_age = 18
print(my_age > 18) # Output : False
print(my_age >= 18) # Output : True
print(my_age < 18) # Output : False

# Boolean Operators

# and operator
print(True and True) # Output : True
print(True and False) # Output : False

# or operator
print(True or False) # Output : True
print(False or False) # Output : False

# MIXING BOOLEAN AND COMPARISION OPERATORS
x,y,z = 5,6,7  
print(x < y and y < z ) # Output : True
print(x < y and y > z) # Output : False
print(x < y or y > z) # Output : True

x,y = 7,8
print(x == y or y == y) # Output : True
print(x == y and y == y) # Output : False

spam = 6
print(3 + 3 == spam and not 3 + 3 == spam + 1) # Output : True