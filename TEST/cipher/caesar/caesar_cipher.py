from cipher.caesar.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        encrypted = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % len(self.alphabet)
                encrypted.append(self.alphabet[output_index])
            else:
                encrypted.append(letter)
        return "".join(encrypted)

    def decrypt_text(self, text: str, key: int) -> str:
        text = text.upper()
        decrypted = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % len(self.alphabet)
                decrypted.append(self.alphabet[output_index])
            else:
                decrypted.append(letter)
        return "".join(decrypted)