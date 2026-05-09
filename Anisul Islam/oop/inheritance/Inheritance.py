class phone:

    def call(self):
        print("you can call me")
    def message(self):
        print("you can message me")
        print("We are from phone class\n")

class Samsung(phone):
    def photo(self):
        print("you can take photo")

s= Samsung()
s.call()
s.message()
s.photo()
s= issubclass(Samsung,phone)
s1= issubclass(phone,Samsung)
print(s)
print(s1)

