from os import remove

num1 ={1,2,3,4,5,5}
print(num1)
num2 = set([4,5,6])
print(f"Before add vale of num2:{num2}")

print("Add value of set num2:")
num2.add(7)
print(f"After add vale:{num2}\n")

num3 = {2,4,6,8}
print(f"Before removing value of set num3:{num3}")
num3.remove(8)
print(f"After removing value of num3:{num3}\n")

print("Check Existing Element:")
print(f"Check Existing Element from num2: {4 in num2}")
print(f"Check Existing Element from num2: {8 in num2}")

print("-----------------------------")
print("Set automatically remove duplicate value")

print("\n-----------------------------")
print("Some operations:")
num4 = {1,2,3,4,5,6}
num5 = set([5,6,7])
print("\nUnion:")
union1 = num4 | num5
print(f"{num4} U {num5}= {union1}")
print("\nIntersection:")
intersection1 = num4 & num5
print(f"{num4} n {num5}= {intersection1}")

print("\nDifference:")
difference = num4 - num5
print(f"{num4} - {num5}= {difference}")


