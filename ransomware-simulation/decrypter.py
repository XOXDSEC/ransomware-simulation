
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes

# Paths
KEY_DIR = "./keys"
TEST_FILES_DIR = "./test_files/encrypted"
DECRYPTED_FILES_DIR = "./test_files/decrypted"
os.makedirs(DECRYPTED_FILES_DIR, exist_ok=True)

# Decrypt files using the private RSA key and AES
def decrypt_file(encrypted_file_path, private_key_path):
    with open(encrypted_file_path, "rb") as f:
        encrypted_content = f.read()

    # Extract the IV, encrypted AES key, and encrypted data
    iv = encrypted_content[:16]
    encrypted_key = encrypted_content[16:16 + 256]  # RSA key size (2048 bits = 256 bytes)
    encrypted_data = encrypted_content[16 + 256:]

    # Load the private RSA key
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    # Decrypt the AES key using the private RSA key
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # Decrypt the data using AES
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Save the decrypted file
    decrypted_file_path = os.path.join(DECRYPTED_FILES_DIR, os.path.basename(encrypted_file_path).replace(".enc", ""))
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    print(f"File '{encrypted_file_path}' decrypted and saved as '{decrypted_file_path}'")

# Main function
def main():
    private_key_path = os.path.join(KEY_DIR, "private_key.pem")

    # Decrypt all files in the encrypted files directory
    for file_name in os.listdir(TEST_FILES_DIR):
        file_path = os.path.join(TEST_FILES_DIR, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            decrypt_file(file_path, private_key_path)

if __name__ == "__main__":
    main()
