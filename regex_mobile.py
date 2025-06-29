import re

pattern=r"^[6-9]\d{9}$"

mobile_number="9871872155"
phone = input("Enter your 10-digit phone number: ")

if re.match(pattern,mobile_number):
    print(f"{mobile_number} is valid mobile number")

else:
    print(f"{mobile_number} is not a validmobile number")