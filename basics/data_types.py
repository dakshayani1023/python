# DATA TYPES 

# Integer
print(-2 + 7)

# floating-point number (float)
print(1.05 + 0.3)

# sum of an integer and a float results in a float .
print(3 + 2.0)

# string 
print('hello')

# string concatenation 
print('key' + 'chain')

# string replication
print('stay' * 3)

# The len() function
print(len('my_name_is_Dakshayani')) # The spaces in the string are also counted as characters by the len() function.

# The str(), int(), and float() functions
print(str(18))        # converts the integer 18 into a string '18'
print(int('26'))      # converts the string '26' into an integer 26
print(float('1.414')) # converts the string '1.414' into a float 1.414

# The type() function 
print(type('Hello'))  # Output: <class 'str'>
print(type(1.414))    # Output: <class 'float'>

# The round() function
print(round(3.14)) 
print(round(1.414222, 3))  # rounds the number to 3 decimal places.
print(round(8.5))          # rounds to the nearest even number.

# The abs() function
print(abs(-5.5))      # Output: 5.5
print(abs(32))        # Output: 32
print(abs(0))         # Output: 0