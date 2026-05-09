import re
pattern = r"color"
text ="My favorite color is blue"
match = re.search(pattern, text)
if match:
    print(match.start()) # print starting character index
    print(match.end()) # print ending character index
    print(match.span())# print starting & ending character index