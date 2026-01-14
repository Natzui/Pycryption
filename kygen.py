from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

asymmetric_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

asymmetric_public_key = asymmetric_private_key.public_key()

with open("private.pem", "wb") as private_file:
    private_file.write(
        asymmetric_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

with open("public.pem", "wb") as public_file:
    public_file.write(
        asymmetric_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Key generation completed.")