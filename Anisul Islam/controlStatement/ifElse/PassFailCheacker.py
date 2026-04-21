mark = int(input("Enter Mark(0 to 100): "))
if mark >=0 and mark <= 100:
    if mark >= 33:
        print("Congratulations!")
        print("You have scored =", mark)
    else:
        print("Try Again!")
        print("You have scored =", mark)
else:
    print("Enter Mark of recommended range")


