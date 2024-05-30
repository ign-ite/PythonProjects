letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(word, shift, list):
    index = []
    shiftedWord = []
    for i in range(len(letters)):
        for j in range(len(word)):
            if (word[j] == letters[i]):
                index.append(i)
    for i in range(len(index)):
        index[i] = int(index[i])
    while (len(shiftedWord) != len(word)):
        for i in range(len(index)):
            if ((index[i]+shift <= 26)):
                print(letters[index[i]])
                shiftedWord.append(letters[index[i]+shift])
                print(shiftedWord[i])
            else:
                print(letters[index[i]])
                shiftedWord.append(letters[shift - (26-index[i])])
                print(shiftedWord[i])
    print(shiftedWord)
userNeed = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
word = input().lower()
word = list(word)
encode(word = word, shift = 5, list = letters)