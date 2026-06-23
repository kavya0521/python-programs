import re
text="DevOps 123"
if re.match(r'^[A-Za-z0-9]+$',text):
    print("Alphanumeric String")
else:
    print("Not Alphanumeric String")
    
