'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)

except (ValueError,ZeroDivisionError):
    print("Either avoid num2= 0 or enter integer")

#except ZeroDivisionError:
 #   print("Division by zero in impossible way")

#except ValueError:
 #   print("Have to insert only integer Number

finally:
    print("Done")
'''

#rase key word use
def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try:
   print(voter(17))
except ValueError as e:
    print(e)
