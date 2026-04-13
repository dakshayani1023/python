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