'''
#This is map function example
def square(x):
    return x*x
num = [1,2,3,4,5]
result = list(map(square,num))
print(result)
'''
#This is filter function example

num = [1,2,3,4,5]
result = list(filter(lambda x: x %2 == 0,num))
print(result)