import re

pattern=r"^\+91[6-9]\d{9}$"

mobile_number= input(" enter your mobile nummber with country code ")

if re.match(pattern,mobile_number):
    print(f"{mobile_number} is valid mobile number")

else:
    print(f"{mobile_number} is not a validmobile number")