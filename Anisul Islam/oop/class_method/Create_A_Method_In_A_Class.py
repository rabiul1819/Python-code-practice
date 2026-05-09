class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, My name is "+self.name)

p1 = person("Emil")
p1.greet()