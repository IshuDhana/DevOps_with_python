3. Regular Expressions for Text Processing
Regular expressions (also known as regex) are a powerful way to identify patterns and process text efficiently.

In Python, the re module provides support for working with regular expressions.

Some commonly used metacharacters include:

. – matches any character

* – matches zero or more occurrences

+ – matches one or more occurrences

? – matches zero or one occurrence

[] – defines a character set

| – acts as an OR operator

^ – matches the beginning of a line

$ – matches the end of a line

Typical use cases include matching email addresses, phone numbers, or extracting specific patterns from text.

The re module offers several useful functions:

re.match() – checks for a match at the beginning of a string

re.search() – searches the entire string for a match

re.findall() – returns all matches in a string

re.sub() – replaces matched patterns with a specified value