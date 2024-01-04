#Reads through a given file to find the three most used words, replace temp[:3] with the desired number
# Open the file 'filename.txt'
fhand = open('filename.txt')

# Create an empty dictionary to store word frequencies
count = dict()

# Iterate through each line in the file
for line in fhand:
    # Split the line into words
    words = line.split()
    
    # Iterate through each word in the line
    for word in words:
        # Update the word count in the dictionary
        count[word] = count.get(word, 0) + 1

# Print the word count dictionary
print(count)

# Create an empty list to store tuples of (frequency, word)
temp = list()

# Iterate through the items (word, frequency) in the count dictionary
for k, v in count.items():
    # Append tuples to the list in the format (frequency, word)
    temp.append((v, k))

# Sort the list of tuples in descending order based on frequency
temp = sorted(temp, reverse=True)

# Iterate through the top two tuples in the sorted list
for val, key in temp[:3]:
    # Print the word and its frequency
    print(key, val)
