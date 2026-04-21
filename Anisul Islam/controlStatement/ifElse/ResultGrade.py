'''mark = int(input("Enter Mark:"))
#if mark >= 80 and mark <= 100:
if 80 <= mark <= 100:#chain comparison
    print("You have scored: A+")
elif 70 <= mark <= 79:
    print("You have scored: A")
elif 60 <= mark <= 69:
    print("You have scored: A-")
elif 50 <= mark <= 59:
    print("You have scored: B")
elif 40 <= mark <= 49:
    print("You have scored: C")
elif 33 <= mark <= 39:
    print("You have scored: D")
else:
    print("Sorry! Try again")
    '''
print("Best version")
mark = int(input("Enter Mark: "))
if not (0 <= mark <= 100):
   print("invalid! Enter a value between 0 and 100")



elif mark >= 80:
    print("You have scored: A+")
elif mark >= 70:
    print("You have scored: A")
elif mark >= 60:
    print("You have scored: A-")
elif mark >= 50:
    print("You have scored: B")
elif mark >= 40:
    print("You have scored: C")
elif mark >= 33:
    print("You have scored: D")
else:
    print("Sorry! Try again")

