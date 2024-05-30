print("Welcome to the Tip Calculator!\n")
bill = float(input("What was the total bill?: "))
tipPerc = int(input("What percentage tip would you like to give? (10, 12, or 15): "))
split = int(input("How many people to split the bill?: "))
billPlusTip = ((tipPerc/100)*bill)+bill
finalShare = billPlusTip/split
print(round(finalShare, 2))