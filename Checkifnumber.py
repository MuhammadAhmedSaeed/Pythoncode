# Purpose: Categorize each element in the input sentence as either an integer or a string.
# Input: User-provided sentence

# Get user input
x = input("Please input any sentence: ")

# Split the sentence into a list of words
y = x.split()

# Iterate through each element in the list
for i in range(len(y)):
    # Check if the element is composed entirely of digits
    if y[i].isdigit():
        # If yes, convert it to an integer
        y[i] = int(y[i])
        # Print that it is a number
        print(y[i], "is number")
    else:
        # Print that it is a string
        print(y[i], "is string")
