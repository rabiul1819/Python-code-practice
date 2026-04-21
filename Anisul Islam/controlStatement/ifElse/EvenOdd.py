num = int(input("Enter a number:"))

if num== 0 :
    print(f"{num} is not either odd or even.")
else:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")