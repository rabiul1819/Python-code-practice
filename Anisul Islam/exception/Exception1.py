#Error
'''
num2 = input("Enter a number:") #here is error cause dividing num to string
result = 40 / num2 # math error dividing by zero
print(result)
print("Done")
'''
#Error
'''
num2 = int(input("Enter a number:"))
result = 40 / num2
print(result)
print("Done")
'''
#Error
'''
text = "Hanifa vi"
print(text[10])
print("Done")
'''

'''
try:
    list = [20,0,3]
    result = list[0] / list[3]
    print(result)
''''''
except ZeroDivisionError:
    print("Division by zero is not possible")
''''''
except IndexError:
    print("Index out of range")
print("Done")
'''
try:
    list = [20,0,3]
    result = list[0] / list[3]
    print(result)

except ZeroDivisionError:
    print("Division by zero is not possible")

#except IndexError:
    # print("Index out of range")
finally:
     print("Done")
     print("Age ki sundor din kataytam amra")
print("Abar ki hoy?")

