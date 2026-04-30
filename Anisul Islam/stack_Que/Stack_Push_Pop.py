books = []
print("Push operation: ")
books.append("C")
books.append("C++")
books.append("Java")
books.append("Python")
print(books)

books.pop()
print("Now the top book is after pop1: ",books[-1])
print(books)

books.pop()
print("Now the top book is after pop2: ",books[-1])
print(books)

books.pop()
print("Now the top book is after pop3: ",books[-1])
print(books)

print("Empty Error handle\n---------------------------")
books.pop()
#print("Now the top book is after pop3: ",books[-1])
if not books:
    print("Out of bound")
