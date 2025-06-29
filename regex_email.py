import re

text="user's email is shubhamrai8361@gmail.com"

match=re.search(r"[a-zA-Z0-9_%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z.-]{2,}",text)

if match:
    print("email is found:",match.group())