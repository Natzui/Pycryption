# 🔐 Hybrid RSA + AES-GCM Encryption System

This project demonstrates a secure communication flow using **RSA** for key exchange and **AES-GCM** for payload encryption.  
It includes scripts for **key generation**, **encryption**, and **decryption**.

---

## 📦 Required Modules

Install the required dependency before running the scripts:

pip install cryptography

---

## 🧪 Running Test Samples

Sender:

python encrypt.py  
Enter message: Hello Dedsec!  
Encrypted: MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A...

Receiver:

python decrypt.py  
Encrypted: MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A...  
Decrypted: Hello DedSec!

