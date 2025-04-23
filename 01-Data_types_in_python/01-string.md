1. String Data Type in Python
A string in Python is a sequence of characters. They are enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
eample :

'''Hello'''

"""Hello"""

2. Strings are immutable.You cannot change a character in a string directly. Instead, you create a new string when you want to make changes.You can access individual characters in a string using indexing.
Example:
my_string[0]

Strings support many built-in methods, such as:

len() – length of the string

upper() – convert to uppercase

lower() – convert to lowercase

strip() – remove whitespace

replace() – replace characters


2. String Manipulation and Formatting
Step 1: Concatenation
You can combine strings using the + operator.
Example:
greeting = "Hello" + " " + "World"

Step 2: Substrings (Slicing)
You can extract parts of a string using slicing.
Example:
my_string = "Python"
print(my_string[2:5])  

Step 3: String Interpolation (Formatting)
Python supports multiple ways to format strings:

f-strings:

name = "Alice"
print(f"Hello, {name}")
% formatting:

print("Hello, %s. You are %d years old." % ("Bob", 30))
str.format() method:

print("Hello, {}.".format("Charlie"))

Step 4: Escape Sequences
Special characters are represented using escape sequences, such as:
\n – new line
\t – tab
\\ – backslash

Example:
print("Hello\nWorld")

Step 5: String Methods for Manipulation
Useful built-in methods include:

split() – split a string into a list
join() – join a list into a string
startswith() – check if a string starts with a substring


