from unittest import result

'''
num = [1,2,3,4,5]
result = list(map(lambda x: x*x,num))
print(result)
'''
# List Comprehensive example
'''
num = [1,2,3,4,5,6]
result = [x*x for x in num]
print(result)
'''
#Filter
'''
num = [1,2,3,4,5,6]
result = list(filter(lambda x: x %2 == 0,num))
print(result)
'''

#Filter to comprehensive list
num = [1,2,3,4,5,6]
result = [x for x in num if x %2 == 0]
print(result)