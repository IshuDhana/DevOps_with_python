import re

text = "DevOps with Python"
pattern = r"with"
replace = "in"

new_text = re.sub(pattern,replace, text)

print("modifyed text:", new_text)
