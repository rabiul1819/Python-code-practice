'''
def calculate(a,b):
    return a*a + 2 *a*b + b*b
print(calculate(3,4))
'''

print("Lamda function is called no name function")
x = (lambda a,b:a*a + 2 *a*b + b*b)(3,4)
print(x)

y = (lambda  x:x*x*x )(3)
print(y)