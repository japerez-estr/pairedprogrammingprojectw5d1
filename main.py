print("AIDEN MCKEE JOSE PEREZ DAVID ROSALES")
#######################paired programmming###############################

# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4:5])
# b. Retrieve the second to last character.
print(magic[-2:-1])
# c. Find the first occurrence of the letter 'c'.
firstoc=magic.find("c")
print(firstoc)
# Advanced Slicing:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet.find("hij"))
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet.find("m"))
print(alphabet[:12:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote 
quote ="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[-1:-16])
# Manipulating Words:
# Given the string info = 
string ="Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(string.find("subjective"))
print(string[36:])
# b. Extract every third word.
print(string[0::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(string[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU."
print(text.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
make = ["Make", "haste", "slowly."]
newthing = ''.join(make)
# b. Now, split the string at every occurrence of the letter 'a'.
print(newthing.split('a'))
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
text2 = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(text2.replace('busy', 'distracted'))
# b. Replace "plans" with "mistakes".
print(text2.replace('plans', 'mistakes'))
# Problem Set 4: String Properties and Advanced Operations
# Repetition: When you use a * sign to print out a text that many times
# Concatenate the word "Iteration" 7 times.
it = 'Iteration'
print(it*7)