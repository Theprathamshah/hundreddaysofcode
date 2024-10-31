totalBill = float(input("What is your total bill?\n"))
people = int(input("What is number of people who are sharing bill\n"))

tipPercentage = int(input("How many percentage of tip you want to give 12, 15, 20?\n"))

billWithTip = (totalBill* tipPercentage//100) + totalBill

payPerPerson = billWithTip / people

print("One person have to contribute {}$".format(payPerPerson))