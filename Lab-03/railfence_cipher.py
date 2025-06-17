import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow  # Đảm bảo bạn đã convert .ui sang .py
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            result = response.json()
            print("Kết quả mã hóa trả về từ API:", result)

            # ✅ Sửa ở đây: dùng đúng key trả về từ API
            if response.status_code == 200 and "encrypted_text" in result:
                self.ui.txt_cipher_text.setText(result["encrypted_text"])
                QMessageBox.information(self, "Thông báo", "Mã hóa thành công!")
            else:
                QMessageBox.warning(self, "Lỗi", f"Lỗi API mã hóa: {result}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi gọi API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }
        try:
            response = requests.post(url, json=payload)
            result = response.json()
            print("Kết quả giải mã trả về từ API:", result)

            if response.status_code == 200 and "decrypted_text" in result:
                self.ui.txt_plain_text.setText(result["decrypted_text"])
                QMessageBox.information(self, "Thông báo", "Giải mã thành công!")
            else:
                error_msg = result.get("error", str(result))
                QMessageBox.warning(self, "Lỗi", f"Lỗi API giải mã: {error_msg}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi gọi API: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
