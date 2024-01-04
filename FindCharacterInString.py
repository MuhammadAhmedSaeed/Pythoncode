#This code asks the user for a text, a specific character
# and counts how many times the character was present
# Ask the user for input text
s = input("Please input your text: ")

# Ask the user for the character to find
p = input('Which character to find: ')

# Initialize a count variable to keep track of the number of times the specified character is found
count = 0

# Iterate through each index in the range of the length of the input text
for i in range(len(s)):
    # Check if the character at the current index is equal to the specified character
    if s[i] == p:
        # Increment the count if the characters match
        count = count + 1

# Print the result indicating how many times the specified character was found in the input text
print(p, 'was found', count, 'times.')
