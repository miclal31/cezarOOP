class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, plaintext):
        encrypted_text = ''
        for char in plaintext.upper():
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.shift) % 26
                encrypted_text += self.alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text

    def decode(self, ciphertext):
        decrypted_text = ''
        for char in ciphertext.upper():
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.shift) % 26
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text


def main():
    shift_value = 3
    cipher = CaesarCipher(shift_value)

    choice = input("What You want do to? (encode/decode): ")
    user_text = input("Input text: ")

    if choice.lower() == 'encode':
        result = cipher.encode(user_text)
        print(f'Encoded Text: {result}')
    elif choice.lower() == 'decode':
        result = cipher.decode(user_text)
        print(f'Decoded Text: {result}')
    else:
        print("Error. Pick 'encode' or 'decode'.")


if __name__ == "__main__":
    main()
