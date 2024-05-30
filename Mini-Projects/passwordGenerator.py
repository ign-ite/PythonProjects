import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letterInPass = []
choose = []
char = ""

for _ in range(nr_letters):
    choose.append(_)

random.shuffle(choose)

for i in range(len(choose)):
    letterInPass.append(letters[choose[i]])

choose.clear()

for _ in range(nr_symbols):
    choose.append(_)

random.shuffle(choose)

for i in range(len(choose)):
    letterInPass.append(symbols[choose[i]])

choose.clear()

for _ in range(nr_numbers):
    choose.append(_)

random.shuffle(choose)

for i in range(len(choose)):
    letterInPass.append(numbers[choose[i]])
    
passwordRand = ""
selectionOrder = []

for i in range(len(letterInPass)):
    selectionOrder.append(i)

random.shuffle(selectionOrder)

print(letterInPass)

for i in range(len(selectionOrder)):
    passwordRand += letterInPass[selectionOrder[i]]

print(f"The password generated is: {passwordRand}")