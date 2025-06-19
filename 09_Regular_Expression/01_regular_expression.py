# Regular Expression 
import re

# text = "My phone number is 9876543210"
# pattern = r"\d{8}"  # match exactly 8 digits

# match = re.search(pattern,text)
# print(match) # <re.Match object; span=(19, 27), match='98765432'>
# print(match.group()) # 98765432

# Uses of Regular Expressions in Python
# 🔹 1. Validation: Validate inputs like email, phone number, PIN code, password, etc.

# email = "test@example.com"
# if re.match(r'^\w+@\w+\.\w+$', email):
#     print("Valid Email")

# 🔹 2. Search in Text: Find specific words, dates, or numbers in large texts.

text = "Date: 12/06/2025"
print(re.search(r"\d{2}/\d{2}/\d{4}", text).group())

# 🔹 3. Data Cleaning:- Remove unwanted characters like symbols, extra spaces, HTML tags.
text = "Hello!!!   "
clean = re.sub(r'[! ]+', '', text)
print(clean)  # Output: Hello

# 🔹 4. Text Extraction: Extract phone numbers, email IDs, URLs, etc. from documents.

print(re.findall(r'\d{10}', "Call me at 9876543210 or 9123456789"))