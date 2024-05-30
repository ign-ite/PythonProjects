print("The Love Calculator is calculating your score....")
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")
word1 = "TRUE"
word2 = "LOVE"
count = 0
for i in range(len(name1)):
    for j in range(4):
        if name1[i] == word1[j]:
            count += 1
for i in range(len(name2)):
    for j in range(4):
        if name2[i] == word1[j]:
            count += 1
for i in range(len(name1)):
    for j in range(4):
        if name1[i] == word2[j]:
            count += 1
for i in range(len(name2)):
    for j in range(4):
        if name2[i] == word2[j]:
            count += 1
if (count < 10) or (count > 90):
    print("Your score is *x*, you go together like coke and mentos.")
elif (40 <= count <= 50):
    print("Your score is *y*, you are alright together.")
else:
    print("You rscore is *z*.")