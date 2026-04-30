'''
thisDict = {"name": "Ford", "Model": "Mustang", "Year": 1964}
#x = thisDict["name"]
print(type(thisDict))

x = thisDict.get("Model")
print(x)
x = thisDict.keys()
print(x)
'''

Car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = Car.keys()

print(x) #before the change

Car["color"] = "white"

print(x) #after the change

x = Car.values()
print(x)
Car["year"] = "2020"
print(x)