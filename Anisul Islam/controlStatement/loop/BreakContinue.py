'''
number = 1
while number <= 100:
    number = number + 1
    print("b4 if ",number)
    if number % 2 == 1:
        continue
    print("After if = ",number)
'''

number = 1
while number <= 100:
    number = number + 1
    print("b4 if ",number)
    if number == 50:
        break
    print("After if = ",number)