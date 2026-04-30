Read_file = open("Read.txt","r+")
#print(Read_file.writable())
'''
read_file = Read_file.read()
print(read_file)
size = len(read_file)
print(size)
'''
'''
text = Read_file.readlines()
print(text)
'''
for x in Read_file:
    print(x)
Read_file.close()