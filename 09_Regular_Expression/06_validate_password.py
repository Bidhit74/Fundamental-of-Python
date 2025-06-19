# 🔸 Q5. Validate password (at least 1 letter, 1 digit, 6+ characters)
import re
password = "Abcd123"
pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$"

if re.search(pattern,password):
    print("Valid Email") 