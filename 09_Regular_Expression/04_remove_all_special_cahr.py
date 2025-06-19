# 🔸 Q3. Remove all special characters
import re
text = "Hello@#123Wor$$$ld!!"
clean = re.sub(r'[^a-z A-Z 0-9]', '', text) # Hello123World
print(clean)
