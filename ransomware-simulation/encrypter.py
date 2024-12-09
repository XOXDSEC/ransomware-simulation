
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import secrets

# Paths
KEY_DIR = "./keys"
TEST_FILES_DIR = "./test_files"
ENCRYPTED_FILES_DIR = "./test_files/encrypted"
os.makedirs(ENCRYPTED_FILES_DIR, exist_ok=True)

# Generate RSA keys if not already present
def generate_rsa_keys():
    private_key_path = os.path.join(KEY_DIR, "private_key.pem")
    public_key_path = os.path.join(KEY_DIR, "public_key.pem")

    if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        with open(private_key_path, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )

        with open(public_key_path, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

# Encrypt files using RSA for the symmetric key and AES for the content
def encrypt_file(file_path, public_key_path):
    with open(file_path, "rb") as f:
        data = f.read()

    # Generate a random AES key and IV
    aes_key = secrets.token_bytes(32)  # AES-256
    iv = secrets.token_bytes(16)      # AES block size is 16 bytes

    # Encrypt the file data using AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(data) + encryptor.finalize()

    # Encrypt the AES key using RSA
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # Save the encrypted data and key
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, os.path.basename(file_path) + ".enc")
    with open(encrypted_file_path, "wb") as f:
        f.write(iv + encrypted_key + encrypted_data)

    print(f"File '{file_path}' encrypted and saved as '{encrypted_file_path}'")

# Main function
def main():
    generate_rsa_keys()
    public_key_path = os.path.join(KEY_DIR, "public_key.pem")

    # Encrypt all files in the test_files directory
    for file_name in os.listdir(TEST_FILES_DIR):
        file_path = os.path.join(TEST_FILES_DIR, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            encrypt_file(file_path, public_key_path)

if __name__ == "__main__":
    main()
