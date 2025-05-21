from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    plain_text = data["plain_text"]
    key = int(data["key"])
    encrypted = caesar.encrypt_text(plain_text, key)
    return jsonify({"encrypted_message": encrypted})

@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    cipher_text = data["cipher_text"]
    key = int(data["key"])
    decrypted = caesar.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_message": decrypted})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)