class phone:
    def __init__(self):
        print("I am from phone Class")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I am from samsung Class")
s1= samsung()
print(s1)