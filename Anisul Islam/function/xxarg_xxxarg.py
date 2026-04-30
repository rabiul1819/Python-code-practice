'''
#xxarg
def student(id,name):
    print(f"Student {id} name: {name}")

student(101,"TR")
'''
def student(*details):
    print(details)

student(101,"Halima")
student(102,"Rashida",64)
