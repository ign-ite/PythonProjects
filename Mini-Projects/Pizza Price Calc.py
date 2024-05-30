print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L: ")
add_pepp = input("Do you want pepporoni? 'Y' or 'N': ")
extra_chess = input("Do you want extra cheese? 'Y' or 'N': ")
bill = 0
if (size == 'S'):
    bill += 15
    if (add_pepp == 'Y'):
        bill += 2
    if (extra_chess == 'Y'):
        bill += 1
elif (size == 'M'):
    bill += 20
    if (add_pepp == 'Y'):
        bill += 3
    if (extra_chess == 'Y'):
        bill += 1
elif (size == 'L'):
    bill += 25
    if (add_pepp == 'Y'):
        bill += 3
    if (extra_chess == 'Y'):
        bill += 1
print(f"Your final bill is: ${bill}.")