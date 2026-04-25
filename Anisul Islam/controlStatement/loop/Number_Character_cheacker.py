number_of_letters = 0
number_of_words = 0
number_of_digits = 0

text = input("Enter text with number and digits: ")
for x in text:
    x = x.lower()
    if x>="a" and x<="z":
       number_of_letters += 1
    elif x>="0" and x<="9":
        number_of_digits += 1
    elif x == " ":
        number_of_words += 1
print("number_of_letters: ",number_of_letters)
print("number_of_digits: ",number_of_digits)
print("number_of_words: ",number_of_words + 1)
