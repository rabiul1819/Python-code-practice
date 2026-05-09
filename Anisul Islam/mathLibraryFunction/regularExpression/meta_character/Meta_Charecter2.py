'''
import re
pattern = r"a*"
if re.match(pattern,"colour"):
    print("Matched")
'''
import re
pattern = r"a+"
if re.match(pattern,"colour"):
    print("Matched")
else:
    print("Not Matched")