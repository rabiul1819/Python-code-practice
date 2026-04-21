import math
from math import sqrt, floor, ceil

result = max(-2,-1,0)
print("Maximum value = " , result)

print("Minimum value = " ,min(-2,-1,0))
print("Abs return non negative  value = " ,abs(-0))
print("X to the power y = " ,pow(-2,-3))
print("Square root = " ,int(sqrt(9)))
print("Round value = " ,round(5.87))
print("Floor value = " ,floor(5.87))
print("Ceiling  value = " ,ceil(5.87))
n = int(input("Enter number of terms for factorial: "))
print(n,"! = " , math.factorial(n))

