# 🔸 Q1. Match a valid phone number (10 digits)
import re
text = "My number is 9876543210"
pattern = r"\d{10}"

print(re.findall(pattern,text))
