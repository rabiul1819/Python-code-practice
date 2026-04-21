'''
ch = input("Enter your choice: ")

if ch == 'a' or ch =='A' or ch == 'e' or ch=='E' or ch == 'i' or ch=='I' or ch == 'o' or ch=='O' or ch == 'u' or ch=='U':
    print(ch,"Vowel")
else:
    print(ch,"Consonant")
'''

ch = input("Enter your choice: ")

if ch.lower() in 'aeiou':
    print(ch, "Vowel")
else:
    print(ch, "Consonant")