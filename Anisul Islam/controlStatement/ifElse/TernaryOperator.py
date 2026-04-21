num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
'''
if  num1 == num2:
    print("The numbers are equal")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")
'''
if num1 == num2:
    print("The numbers are equal")
else:
  print(f"{num1} is grater than {num2}" if num1 > num2 else f"{num2} is greater than {num1}")


