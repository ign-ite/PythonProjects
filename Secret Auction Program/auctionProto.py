import os

moreBidders = "yes"
bidderDict = {}
count = 0

while moreBidders == "yes":
    os.system('cls')
    if count == 0:
        print("Welcome to the secret auction program.") 
        count = 1   
    bidderName = input("Enter Bidder Name: ")
    bidderPrice = float(input("Enter Bid Price: "))        
    bidderDict[bidderName] = bidderPrice
    moreBidders = input("Are there any other bidders?: ")

max = 0
nameWinner = ""
for i in bidderDict:    
    if bidderDict[i] >= max:
        max = bidderDict[i]
        nameWinner = i

print(f"{nameWinner} has the highest bid!")