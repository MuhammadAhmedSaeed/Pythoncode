#This code asks the user for a text, a specific character
# and counts how many times the character was present
s = input("Please input your text")
p=input('Which character to find: ')
#count variable to keep note of the times the requested variable is found
count = 0
for i in range(len(s)):
    if s[i] == p:
        count = count+1
print(p,'was found', count, 'times.')
