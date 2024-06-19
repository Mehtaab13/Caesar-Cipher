import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alphabet_upper = []
for letter in alphabet:
    alphabet_upper.append(letter.upper())

rerun = 0

while rerun == 0:
    print(logo.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))


    def encrypt(text_to_encrypt, shift_amount):
        word = ""
        for character in text_to_encrypt:
            if character.islower():
                position = alphabet.index(character)
                new_position = position + shift_amount
                if new_position >= len(alphabet):
                    new_position %= 26
                word += alphabet[new_position]
            elif character.isupper():
                position = alphabet_upper.index(character)
                new_position = position + shift_amount
                if new_position >= len(alphabet_upper):
                    new_position %= 26
                word += alphabet_upper[new_position]
            else:
                word += character
        print("Encoded word: " + word)


    def decrypt(text_to_decrypt, shift_amount):
        word = ""
        for character in text_to_decrypt:
            if character.islower():
                position = alphabet.index(character)
                new_position = position - shift_amount
                if new_position < 0:
                    new_position += 26
                word += alphabet[new_position]
            elif character.isupper():
                position = alphabet_upper.index(character)
                new_position = position - shift_amount
                if new_position < 0:
                    new_position += 26
                word += alphabet_upper[new_position]
            else:
                word += character
        print("Decoded word: " + word)


    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    again = input("Type 'yes' if you would like to rerun, else type 'no': ")

    if again == 'yes':
        rerun = 0
    else:
        rerun = 1
