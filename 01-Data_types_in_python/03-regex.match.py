import re

text = "DevOps with Python"
pattern = r"with"

match = re.match(pattern, text)


if match:
    print("Pattern found", match.group())
else:
    print("pattern not found")
