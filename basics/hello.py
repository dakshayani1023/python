# This program says hello and asks for my name . 

print('Hello, world!')
print('What is your name?')
my_name = input('>') # We can use input() to get user input and store it in a variable .
print('It is good to meet you,'+ my_name)
print('The length of your name is :')
print(len(my_name)) # We can use len() to get the lenght of a string.
print('What is your age?')
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year ') # Since my age is a string, we need to convert it into a number using int() beforewe add it to one and then convert back into a string using str() to concatinate it with the rest of the sentence. 


