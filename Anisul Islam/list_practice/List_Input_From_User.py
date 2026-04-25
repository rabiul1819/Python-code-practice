n = input("Enter a text of number ")
list1 = n.split() # split() convert a string into a list of values

sum = 0
for num in list1:
    sum += int(num) # Why use int() inside loop?
# Because split() gives strings, not numbers
print(f"Sum = {sum}")