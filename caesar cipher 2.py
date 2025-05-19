def encrypt_caesar(message, shift_value):
    encrypted_text = []
    for char in message:
        if char.islower():
            shifted = (ord(char) - 97 + shift_value) % 26 + 97
            encrypted_text.append(chr(shifted))
        elif char.isupper():
            shifted = (ord(char) - 65 + shift_value) % 26 + 65
            encrypted_text.append(chr(shifted))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt_caesar(cipher_text, shift_value):
    return encrypt_caesar(cipher_text, -shift_value)

# Main execution
if __name__ == "__main__":
    print("=== Caesar Cipher Tool ===")
    original_text = input("Type your message: ")
    shift_amount = int(input("Shift amount (e.g., 3): "))

    coded = encrypt_caesar(original_text, shift_amount)
    decoded = decrypt_caesar(coded, shift_amount)

    print("\nEncrypted:", coded)
    print("Decrypted:", decoded)
