# 🔸 Q2. Match a valid email address
import re
email = "abc123@gmail.com"
pattern = r"^\w+@\w+\.+\w+$"

if re.search(pattern,email):
    print("Valid Email") 

else:
    print("Invalid Email")