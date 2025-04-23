import re

text = "DevOps with Python"
pattern = r"with"

search = re.search(pattern, text)


if search:
    print("Pattern found", search.group())
else:
    print("pattern not found")
