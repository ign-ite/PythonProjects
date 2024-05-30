letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(word, shift, alphabets):
    word = list(word)
    cipherWord = ""
    for char in word:
        if char not in alphabets:
            cipherWord += word[word.index(char)]
        elif (alphabets.index(char) + shift <= len(alphabets)):
            cipherWord += alphabets[alphabets.index(char)+shift]
        elif (alphabets.index(char) + shift > len(alphabets)):
            cipherWord += alphabets[shift - (len(alphabets) - alphabets.index(char))]
    return cipherWord
programLoop = 1
while programLoop == 1:
    userNeed = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    userWord = input(f"Enter your word to {userNeed}: ").lower()
    userShift = int(input("Enter the shift: "))
    if userNeed == 'encode':    
        shiftedWord = encode(word = userWord, shift = userShift, alphabets= letters)
        print(shiftedWord)
        programLoop = int(input("Do you want to encrypt/decrypt again?(Press 1 for Yes, 0 for No): "))
    elif userNeed == 'decode':
        shiftedWord = encode(word = userWord, shift = -userShift, alphabets= letters)
        print(shiftedWord)
        programLoop = int(input("Do you want to encrypt/decrypt again?(Press 1 for Yes, 0 for No): "))
    else:
        print("Enter a valid input as to whether to encode or decode!")
        programLoop = int(input("Do you want to encrypt/decrypt again?(Press 1 for Yes, 0 for No): "))