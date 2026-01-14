from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes, serialization
import os, base64

with open("public.pem", "rb") as public_file:
    recipient_public_key = serialization.load_pem_public_key(public_file.read())

plain_input_data = input("Enter message: ").encode()

session_symmetric_key = AESGCM.generate_key(bit_length=256)
session_nonce = os.urandom(12)

aes_engine = AESGCM(session_symmetric_key)
encrypted_payload = aes_engine.encrypt(session_nonce, plain_input_data, None)

encrypted_session_key = recipient_public_key.encrypt(
    session_symmetric_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

final_transport_blob = base64.b64encode(
    encrypted_session_key + session_nonce + encrypted_payload
).decode()

print("Encrypted:", final_transport_blob)