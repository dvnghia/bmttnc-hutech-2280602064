import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class VigenereCipherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        plain_text = self.ui.txt_plain_text.toPlainText()
        key = self.ui.txt_key.text()

        if not key.isalpha():
            QMessageBox.warning(self, "Lỗi", "Key chỉ được chứa chữ cái (A-Z, a-z)!")
            return

        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }

        try:
            res = requests.post(url, json=payload)
            data = res.json()
            cipher = data.get("encrypted_text") or data.get("encrypted_message")
            if res.ok and cipher:
                self.ui.txt_cipher_text.setText(cipher)
                QMessageBox.information(self, "Thành công", "Mã hóa thành công!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Lỗi API mã hóa: {data}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

    def decrypt(self):
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.text()

        if not key.isalpha():
            QMessageBox.warning(self, "Lỗi", "Key chỉ được chứa chữ cái (A-Z, a-z)!")
            return

        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }

        try:
            res = requests.post(url, json=payload)
            data = res.json()
            plain = data.get("decrypted_text") or data.get("decrypted_message")
            if res.ok and plain:
                self.ui.txt_plain_text.setText(plain)
                QMessageBox.information(self, "Thành công", "Giải mã thành công!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Lỗi API giải mã: {data}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VigenereCipherApp()
    win.show()
    sys.exit(app.exec_())
