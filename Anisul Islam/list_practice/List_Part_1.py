
subject = ["C","C++","C#","Java","Python","JavaScript","HTML","MySQL"]
# print(subject) # print all element from zero to last
# print("Print from 2 to last: ",subject[2:])

# print("Print last element : ",subject[-1])
'''
i = 0
print("Subject len: ",len(subject))
while i < len(subject):
  print(subject[i])
  i += 1
'''
print("Original list:")
print(subject)
print("Check is element exist in the list?")
print("Python" in subject)# python is Case sensitive
print("python" in subject)# python is Case sensitive
print("Parl" in subject)
print("Parl" not in subject)
print("Add element to list")
print(subject + ["Swift","27","5.5"])