from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, serialization
import base64

with open("private.pem", "rb") as private_file:
    local_private_key = serialization.load_pem_private_key(
        private_file.read(),
        password=None
    )

received_blob = base64.b64decode(input("Encrypted: "))

encrypted_session_key = received_blob[:256]
received_nonce = received_blob[256:268]
received_ciphertext = received_blob[268:]

session_symmetric_key = local_private_key.decrypt(
    encrypted_session_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

aes_engine = AESGCM(session_symmetric_key)
decrypted_output = aes_engine.decrypt(
    received_nonce,
    received_ciphertext,
    None
)

print("Decrypted:", decrypted_output.decode())