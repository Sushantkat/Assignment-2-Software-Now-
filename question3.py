# Key for decryption
zl_qvpg = {"xrl1": "inyhr1", "xrl2": "inyhr2", "xrl3": "inyhr3", "xrl4": "inyhr4"}

# Function to decrypt the code
def decrypt_code(encrypted_code, key):
    decrypted_code = encrypted_code
    
    for xrl, inyhr in key.items():
        decrypted_code = decrypted_code.replace(inyhr, xrl)

    return decrypted_code