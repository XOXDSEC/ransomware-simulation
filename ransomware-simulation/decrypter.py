
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes

KEY_DIR = "./keys"
TEST_FILES_DIR = "./test_files/encrypted"
DECRYPTED_FILES_DIR = "./test_files/decrypted"
os.makedirs(DECRYPTED_FILES_DIR, exist_ok=True)

def decrypt_file(encrypted_file_path, private_key_path):
    with open(encrypted_file_path, "rb") as f:
        encrypted_content = f.read()

    iv = encrypted_content[:16]
    encrypted_key = encrypted_content[16:16 + 256] 
    encrypted_data = encrypted_content[16 + 256:]

    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

   
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

   
    decrypted_file_path = os.path.join(DECRYPTED_FILES_DIR, os.path.basename(encrypted_file_path).replace(".enc", ""))
    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)

    print(f"File '{encrypted_file_path}' decrypted and saved as '{decrypted_file_path}'")


def main():
    private_key_path = os.path.join(KEY_DIR, "private_key.pem")

    
    for file_name in os.listdir(TEST_FILES_DIR):
        file_path = os.path.join(TEST_FILES_DIR, file_name)
        if os.path.isfile(file_path):  # Ensure it's a file
            decrypt_file(file_path, private_key_path)

if __name__ == "__main__":
    main()
