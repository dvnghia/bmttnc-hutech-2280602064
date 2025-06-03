class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, plain_text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(plain_text):
                encrypted_text += plain_text[pointer]  # Sửa text -> plain_text
                pointer += key
        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Tính số hàng (rows)
        num_rows = len(cipher_text) // key
        if len(cipher_text) % key != 0:
            num_rows += 1

        num_full_cols = len(cipher_text) % key
        plaintext = [''] * num_rows

        col = 0
        row = 0
        for symbol in cipher_text:
            plaintext[row] += symbol
            row += 1

            if (row == num_rows) or (row == num_rows - 1 and col >= num_full_cols):
                row = 0
                col += 1

        return ''.join(plaintext)
