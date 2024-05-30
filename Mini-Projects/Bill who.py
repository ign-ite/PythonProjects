import random
name_string = input("Enter the names: ")
names = name_string.split(" ")
rand = random.randint(0, len(names)-1)
print(f"{names[rand]} has to pay the bill!")