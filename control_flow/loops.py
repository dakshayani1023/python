# ------------ Control flow with loops ------------
spam = 0
if spam < 5: 
    print("I am sleepy")
    spam = spam + 1
# Output: I am sleepy, because the condition spam < 5 is true. The value of spam is then incremented by 1, but since the code is not in a loop, it will not check the condition again and will not print anything else.

spam = 0
while spam < 5:
    print("I am not sleepy")
    spam = spam + 1 
# Output: I am not sleepy, printed 5 times, because the while loop continues to execute as long as the condition spam < 5 is true. The value of spam is incremented by 1 in each iteration(i.e, each time the loop is executed), and once it reaches 5, the condition becomes false and the loop terminates.


# ----------- An annoying while loop ----------
name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
print("Thank you!") # Un-indented, so it is not part of the while loop and will only be executed once the loop has terminated i.e, once the condition becomes false.
# In this code, the while loop will continue to prompt the user to "Please type your name." until the user types "your name". Once the user types "your name", the condition name != "your name" becomes false, and the loop terminates. After the loop has terminated, it will print "Thank you!".

# ----------- break statement ---------

while True: # This creates an infinite loop because the condition is always true.
    print("Please enter your name.")
    name = input()
    if name == "Ellie":
        break # This will exit the loop when the user types "Ellie".
print("Thank you!") # This will be executed after the loop is exited, which happens when the user types "Ellie".

# ----------- continue statement ---------
while True:
    print("Who are you?")
    name = input()
    if name != "Raya":
        continue # This will skip the rest of the loop and start the next iteration if the user does not type "Raya".
    print("Hello, Raya. What is the password? (It is a bird.)")
    password = input()
    if password == "Falcon":
        break # This will exit the loop when the user types "Falcon" as the password.
print("Access granted.") # This will be executed after the loop is exited, which happens when the user types "Raya" as the name and "Falcon" as the password.

# ------------ Truthy and Falsy values ------------
name = ''
while not name: # This condition will be true as long as name is an empty string or contains only whitespace characters, which are considered falsy values in Python.
    print('Enter your name:') # 
    name = input()
print('How many guests will you have?')
num_of_guests = int(input()) # This will convert the user input into an integer and store it in the variable num_of_guests.
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')

# ------------ Examples of truthy and falsy values --------

print(bool(' ')) # This will print True because a string with a space is considered a truthy value in Python.
print(bool(''))  # This will print False because an empty string is considered a falsy value in Python.
print(bool(0))   # This will print False because the integer 0 is considered a falsy value in Python.

# ------------ for Loops and the range() function ------------
print("Hello!")
for i in range(7):
    print('On this iteration, i is set to ' + str(i))
print("Goodbye!") # This is NOT indented, so it runs once after the loop has finished executing. The for loop will iterate 7 times, with i taking on the values from 0 to 6, and it will print the message with the current value of i in each iteration. After the loop is done, it will print "Goodbye!".

# ------------ Adding numbers upto 100 ------------

total = 0
for i in range(101):
    total = total + i
print(total)