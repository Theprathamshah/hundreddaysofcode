print("Welcome to the Love Calculator!")
name1 = input("What's your name? \n")
name2 = input("What's their name? \n")

combinedName = name1 + name2

lowercasedName = combinedName.lower()

t = lowercasedName.count('t')
r = lowercasedName.count('r')
u = lowercasedName.count('u')
e = lowercasedName.count('e')
l = lowercasedName.count('l')
o = lowercasedName.count('o')
v = lowercasedName.count('v')
e = lowercasedName.count('e')

true = t + r + u + e
love = l + o + v + e

loveScore = int(str(true) + str(love))
score = true + love

print("Your love score is string  {} and {}".format(loveScore,score))

if loveScore < 10 or loveScore > 90:
    print(f"Your love score is {loveScore}, you go togather like coke and mentos.")
elif loveScore >= 40 and loveScore<=50 :
    print(f"Your love score is {loveScore}, you guys are alright together")
else: 
    print(f"Your love score is {loveScore}")