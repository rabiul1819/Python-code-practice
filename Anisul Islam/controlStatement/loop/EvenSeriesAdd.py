'''
# 2 + 4 + 6 + 8+........
startNo = 2
total = 0
endNo = int(input("Enter the range of the series: 2 + 4 + 6 + 8+........+ = "))
while startNo <= endNo:
      total += startNo
      startNo += 2
print("Sum of the series: ", total)
print("No check for Odd number! ")
'''
from selectors import SelectSelector

# 2 + 4 + 6 + 8+........
startNo = 2
total = 0
endNo = int(input("Enter the range of the series: 2 + 4 + 6 + 8+........+ = "))
if endNo % 2 != 0:
      print("Ops! Enter any even number")
else:
      while startNo <= endNo:
            total += startNo
            startNo += 2
      print("Sum of the series: ", total)
      print("I have checked for Odd number! ")

'''
#Gchat gpt recommend best option 
startNo = 2
total = 0

endNo = int(input("Enter the range: "))

if endNo % 2 != 0:
    print("Odd number entered, adjusting to nearest even...")
    endNo -= 1

while startNo <= endNo:
    total += startNo
    startNo += 2

print("Sum of even series:", total)
'''