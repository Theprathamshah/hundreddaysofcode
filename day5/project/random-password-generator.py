import random
lowercaseLetter = 'abcdefghijkmlnopqrstuvwxyz'
uppercaseLetter = lowercaseLetter.upper()
numbers = '123456789'
punctuation = '!@#$%^&*-'
passwordLength = int(input("Enter length of password\n"))
isNumbers = int(input("You want numbers in password"))
isPunctuation = int(input("You want punctuation in password"))
password = ''

passwordString = lowercaseLetter + uppercaseLetter

if isNumbers:
    passwordString += numbers
if isPunctuation:
    passwordString += punctuation

for i in range(0,passwordLength):
    randomIndex = random.randint(0,len(passwordString))
    password = password + passwordString[randomIndex]
print(f"Random password is {password}")