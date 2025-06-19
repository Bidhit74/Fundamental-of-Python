# 🔸 Q4. Find all words that start with capital letters
import re

text = "India is my Country"
pattern = r"\b[A-Z][a-z]*\b"
print(re.findall(pattern, text))