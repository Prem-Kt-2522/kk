# Encryption function
def encrypt_message(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

# Decryption function
def decrypt_message(encrypted_message, reversed_dict):
    decrypted_message = []
    for letter in encrypted_message:
        decrypted_message.append(reversed_dict.get(letter, letter))
    return ''.join(decrypted_message)

# Monoalphabetic cipher dictionary
monoalpha_cipher = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i',
    'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h',
    'q': 'j', 'r': 'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
    'y': 'n', 'z': 'm'
}

# Create reversed cipher dictionary for decryption
reversed_dict = {value: key for key, value in monoalpha_cipher.items()}

# Original message
message = "hello world"

# Encrypt the message
encrypted_message = encrypt_message(message, monoalpha_cipher)

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, reversed_dict)

# Print results
print("Rollno: 2453021")
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
