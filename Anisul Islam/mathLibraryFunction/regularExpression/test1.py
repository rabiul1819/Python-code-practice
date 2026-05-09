import re
pattern = r"Color"
#if re.match(pattern,"Blue is a color,I love blue color"):
#if re.search(pattern,"Blue is a color,I love blue Color"):
print(re.findall(pattern, r"Color"))
