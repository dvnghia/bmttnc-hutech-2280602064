class PlayFairCipher:
    def __init__(self):
        pass


    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        seen = set()
        matrix = []

        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                matrix.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, letter, matrix):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None

    def preprocess_text(self, text):
        text = text.replace("J", "I").upper()
        processed = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = ''
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    b = 'X'
                    i += 1
                else:
                    i += 2
            else:
                b = 'X'
                i += 1
            processed += a + b
        return processed

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.preprocess_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i + 1]
            row1, col1 = self.find_letter_coords(a, matrix)
            row2, col2 = self.find_letter_coords(b, matrix)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_coords(a, matrix)
            row2, col2 = self.find_letter_coords(b, matrix)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        return decrypted_text
